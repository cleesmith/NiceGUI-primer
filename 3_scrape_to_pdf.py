# ***
# NOT recommended for use with AI, as plain text is smaller, faster, and easier to ingest
# ***
from playwright.sync_api import sync_playwright
import io
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

MAX_PAGE_HEIGHT_MM = 5080  # Maximum height per ISO 32000 standard
MAX_WIDTH = 0
MAX_HEIGHT = 0

def get_page_height(page, url):
	global MAX_WIDTH, MAX_HEIGHT
	page.goto(url)
	height_px = page.evaluate("document.body.scrollHeight")
	height_mm = round(height_px * 0.264583, 2)  # convert pixels to millimeters and round to 2 decimal places
	# Smallest Value
	#     203.2mm for the URL: http://localhost:8080/documentation/page_title
	# Average Value
	#     2558.05mm (calculated by summing all heights and dividing by the number of entries)
	# Largest Value
	#     8854.27mm for the URL: http://localhost:8080/documentation/page_layout
	width_px = page.evaluate("document.body.scrollWidth")
	width_mm = round(width_px * 0.264583, 2)
	print(f"width: {width_mm}mm x height: {height_mm}mm = {url}")
	if width_mm > MAX_WIDTH:
		MAX_WIDTH = width_mm
	if height_mm > MAX_HEIGHT:
		MAX_HEIGHT = height_mm
	return height_mm

def add_page_to_pdf(page, url, pdf_writer):
	# print(url)
	page.goto(url)
	page.emulate_media(media="screen")

	height_mm = get_page_height(page, url)
	if height_mm > MAX_PAGE_HEIGHT_MM:
		height_mm = MAX_PAGE_HEIGHT_MM

	pdf_buffer = page.pdf(
		# width='210mm',  # standard A4 width
		width='375mm',
		height=f'{height_mm}mm',  # dynamically set the height
		print_background=False,
		margin={
			'top': '0in',
			'right': '0in',
			'bottom': '0in',
			'left': '0in'
		},
		scale=1
	)
	
	pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_buffer))
	for page_num in range(len(pdf_reader.pages)):
		pdf_writer.add_page(pdf_reader.pages[page_num])

def add_end_page(pdf_writer):
	packet = io.BytesIO()
	can = canvas.Canvas(packet, pagesize=letter)
	can.setFont("Helvetica", 48)
	can.drawString(200, 400, "The End")
	can.save()

	packet.seek(0)
	new_pdf = PyPDF2.PdfReader(packet)
	pdf_writer.add_page(new_pdf.pages[0])

def generate_pdf(output_path):
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch()
		page = browser.new_page()
		pdf_writer = PyPDF2.PdfWriter()

		urls = []
		with open("urls_to_crawl.txt", "r") as file:
			# read all lines from the file and strip any leading/trailing whitespace
			urls = [line.strip() for line in file]

		for url in urls:
			add_page_to_pdf(page, url, pdf_writer)
			time.sleep(0.5)  # slow down to avoid errors on localhost:8080

		browser.close()

		# add the final "The End" page
		add_end_page(pdf_writer)

		with open(output_path, 'wb') as output_pdf:
			pdf_writer.write(output_pdf)

if __name__ == "__main__":
	import time
	start_time = time.time()

	pdf_file = 'nicegui_documentation.pdf'
	generate_pdf(pdf_file)

	overall_time = time.time() - start_time
	print(f"Crawling time: {overall_time:.2f} sec.s to create {pdf_file}")
	print(f"MAX_WIDTH={MAX_WIDTH}")
	print(f"MAX_HEIGHT={MAX_HEIGHT}")

# Aug 4, 2024:
# Crawling time: 113.81 sec.s to create nicegui_documentation.pdf
# MAX_WIDTH=369.36
# MAX_HEIGHT=8346.01

