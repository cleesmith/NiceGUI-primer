# from playwright.sync_api import sync_playwright
# import io
# import PyPDF2

# def add_page_to_pdf(page, url, pdf_writer):
#     print(url)
#     page.goto(url)
#     page.emulate_media(media="screen")

#     # pdf_buffer = page.pdf(format='A4', print_background=False)

#     # try a very long custom paper size to create a nearly continuous scroll
#     pdf_buffer = page.pdf(
#         width='210mm',  # standard A4 width
#         height='3672.10mm',  # custom height, adjust as needed for fewer page breaks
#         print_background=False,
#         margin={
#             'top': '0in',
#             'right': '0in',
#             'bottom': '0in',
#             'left': '0in'
#         },
#         scale=1
#     )
    
#     pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_buffer))
#     for page_num in range(len(pdf_reader.pages)):
#         pdf_writer.add_page(pdf_reader.pages[page_num])

# def generate_pdf(output_path):
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch()
#         page = browser.new_page()
#         pdf_writer = PyPDF2.PdfWriter()

#         # List of local URLs to scrape and convert to PDF
#         urls = [
#             "http://localhost:8080/documentation/",
#             "http://localhost:8080/documentation/section_text_elements",
#             "http://localhost:8080/documentation/section_controls",
#             "http://localhost:8080/documentation/section_audiovisual_elements",
#             "http://localhost:8080/documentation/section_data_elements",
#             "http://localhost:8080/documentation/section_binding_properties",
#             "http://localhost:8080/documentation/section_page_layout",
#             "http://localhost:8080/documentation/section_styling_appearance",
#             "http://localhost:8080/documentation/section_action_events",
#             "http://localhost:8080/documentation/section_pages_routing",
#             "http://localhost:8080/documentation/section_configuration_deployment",
#             "http://localhost:8080/documentation/label",
#             "http://localhost:8080/documentation/link",
#             "http://localhost:8080/documentation/chat_message",
#             "http://localhost:8080/documentation/element",
#             "http://localhost:8080/documentation/markdown",
#             "http://localhost:8080/documentation/restructured_text",
#             "http://localhost:8080/documentation/mermaid",
#             "http://localhost:8080/documentation/html",
#             "http://localhost:8080/documentation/image",
#             "http://localhost:8080/documentation/button",
#             "http://localhost:8080/documentation/button_group",
#             "http://localhost:8080/documentation/button_dropdown",
#             "http://localhost:8080/documentation/badge",
#             "http://localhost:8080/documentation/chip",
#             "http://localhost:8080/documentation/toggle",
#             "http://localhost:8080/documentation/radio",
#             "http://localhost:8080/documentation/select",
#             "http://localhost:8080/documentation/checkbox",
#             "http://localhost:8080/documentation/switch",
#             "http://localhost:8080/documentation/slider",
#             "http://localhost:8080/documentation/range",
#             "http://localhost:8080/documentation/joystick",
#             "http://localhost:8080/documentation/input",
#             "http://localhost:8080/documentation/textarea",
#             "http://localhost:8080/documentation/codemirror",
#             "http://localhost:8080/documentation/number",
#             "http://localhost:8080/documentation/knob",
#             "http://localhost:8080/documentation/color_input",
#             "http://localhost:8080/documentation/color_picker",
#             "http://localhost:8080/documentation/date",
#             "http://localhost:8080/documentation/time",
#             "http://localhost:8080/documentation/upload",
#             "http://localhost:8080/documentation/teleport",
#             "http://localhost:8080/documentation/interactive_image",
#             "http://localhost:8080/documentation/audio",
#             "http://localhost:8080/documentation/video",
#             "http://localhost:8080/documentation/icon",
#             "http://localhost:8080/documentation/avatar",
#             "http://localhost:8080/documentation/table",
#             "http://localhost:8080/documentation/aggrid",
#             "http://localhost:8080/documentation/echart",
#             "http://localhost:8080/documentation/pyplot",
#             "http://localhost:8080/documentation/matplotlib",
#             "http://localhost:8080/documentation/line_plot",
#             "http://localhost:8080/documentation/plotly",
#             "http://localhost:8080/documentation/linear_progress",
#             "http://localhost:8080/documentation/circular_progress",
#             "http://localhost:8080/documentation/spinner",
#             "http://localhost:8080/documentation/scene",
#             "http://localhost:8080/documentation/leaflet",
#             "http://localhost:8080/documentation/tree",
#             "http://localhost:8080/documentation/log",
#             "http://localhost:8080/documentation/editor",
#             "http://localhost:8080/documentation/code",
#             "http://localhost:8080/documentation/json_editor",
#             "http://localhost:8080/documentation/storage",
#             "http://localhost:8080/documentation/page",
#             "http://localhost:8080/documentation/card",
#             "http://localhost:8080/documentation/column",
#             "http://localhost:8080/documentation/row",
#             "http://localhost:8080/documentation/grid",
#             "http://localhost:8080/documentation/list",
#             "http://localhost:8080/documentation/expansion",
#             "http://localhost:8080/documentation/scroll_area",
#             "http://localhost:8080/documentation/separator",
#             "http://localhost:8080/documentation/space",
#             "http://localhost:8080/documentation/skeleton",
#             "http://localhost:8080/documentation/splitter",
#             "http://localhost:8080/documentation/tabs",
#             "http://localhost:8080/documentation/stepper",
#             "http://localhost:8080/documentation/timeline",
#             "http://localhost:8080/documentation/carousel",
#             "http://localhost:8080/documentation/pagination",
#             "http://localhost:8080/documentation/menu",
#             "http://localhost:8080/documentation/context_menu",
#             "http://localhost:8080/documentation/tooltip",
#             "http://localhost:8080/documentation/notify",
#             "http://localhost:8080/documentation/notification",
#             "http://localhost:8080/documentation/dialog",
#             "http://localhost:8080/documentation/query",
#             "http://localhost:8080/documentation/colors",
#             "http://localhost:8080/documentation/dark_mode",
#             "http://localhost:8080/documentation/add_style",
#             "http://localhost:8080/documentation/timer",
#             "http://localhost:8080/documentation/keyboard",
#             "http://localhost:8080/documentation/refreshable",
#             "http://localhost:8080/documentation/generic_events",
#             "http://localhost:8080/documentation/run_javascript",
#             "http://localhost:8080/documentation/clipboard",
#             "http://localhost:8080/documentation/page_layout",
#             "http://localhost:8080/documentation/page_title",
#             "http://localhost:8080/documentation/navigate",
#             "http://localhost:8080/documentation/download",
#             "http://localhost:8080/documentation/run",
#         ]

#         for url in urls:
#             add_page_to_pdf(page, url, pdf_writer)
#             time.sleep(0.5) # slow down to avoid errors on localhost:8080

#         browser.close()

#         with open(output_path, 'wb') as output_pdf:
#             pdf_writer.write(output_pdf)

# if __name__ == "__main__":
#     import time
#     start_time = time.time()    

#     pdf_file = 'zzz9_merged_output.pdf'
#     generate_pdf(pdf_file)

#     overall_time = time.time() - start_time
#     print(f"Crawling time: {overall_time:.2f} sec.s to create {pdf_file}")



# from playwright.sync_api import sync_playwright
# import io
# import PyPDF2
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# def add_page_to_pdf(page, url, pdf_writer):
#     print(url)
#     page.goto(url)
#     page.emulate_media(media="screen")

#     # pdf_buffer = page.pdf(format='A4', print_background=False)

#     # try a very long custom paper size to create a nearly continuous scroll
#     pdf_buffer = page.pdf(
#         width='210mm',  # standard A4 width
#         height='3672.10mm',  # custom height, adjust as needed for fewer page breaks
#         print_background=False,
#         margin={
#             'top': '0in',
#             'right': '0in',
#             'bottom': '0in',
#             'left': '0in'
#         },
#         scale=1
#     )
    
#     pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_buffer))
#     for page_num in range(len(pdf_reader.pages)):
#         pdf_writer.add_page(pdf_reader.pages[page_num])

# def add_end_page(pdf_writer):
#     packet = io.BytesIO()
#     can = canvas.Canvas(packet, pagesize=letter)
#     can.setFont("Helvetica", 48)
#     can.drawString(200, 400, "The End")
#     can.save()

#     packet.seek(0)
#     new_pdf = PyPDF2.PdfReader(packet)
#     pdf_writer.add_page(new_pdf.pages[0])

# def generate_pdf(output_path):
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch()
#         page = browser.new_page()
#         pdf_writer = PyPDF2.PdfWriter()

#         # List of local URLs to scrape and convert to PDF
#         urls = [
#             "http://localhost:8080/documentation/",
#             "http://localhost:8080/documentation/section_text_elements",
#             "http://localhost:8080/documentation/section_controls",
#             "http://localhost:8080/documentation/section_audiovisual_elements",
#             "http://localhost:8080/documentation/section_data_elements",
#             "http://localhost:8080/documentation/section_binding_properties",
#             "http://localhost:8080/documentation/section_page_layout",
#             "http://localhost:8080/documentation/section_styling_appearance",
#             "http://localhost:8080/documentation/section_action_events",
#             "http://localhost:8080/documentation/section_pages_routing",
#             "http://localhost:8080/documentation/section_configuration_deployment",
#             "http://localhost:8080/documentation/label",
#             "http://localhost:8080/documentation/link",
#             "http://localhost:8080/documentation/chat_message",
#             "http://localhost:8080/documentation/element",
#             "http://localhost:8080/documentation/markdown",
#             "http://localhost:8080/documentation/restructured_text",
#             "http://localhost:8080/documentation/mermaid",
#             "http://localhost:8080/documentation/html",
#             "http://localhost:8080/documentation/image",
#             "http://localhost:8080/documentation/button",
#             "http://localhost:8080/documentation/button_group",
#             "http://localhost:8080/documentation/button_dropdown",
#             "http://localhost:8080/documentation/badge",
#             "http://localhost:8080/documentation/chip",
#             "http://localhost:8080/documentation/toggle",
#             "http://localhost:8080/documentation/radio",
#             "http://localhost:8080/documentation/select",
#             "http://localhost:8080/documentation/checkbox",
#             "http://localhost:8080/documentation/switch",
#             "http://localhost:8080/documentation/slider",
#             "http://localhost:8080/documentation/range",
#             "http://localhost:8080/documentation/joystick",
#             "http://localhost:8080/documentation/input",
#             "http://localhost:8080/documentation/textarea",
#             "http://localhost:8080/documentation/codemirror",
#             "http://localhost:8080/documentation/number",
#             "http://localhost:8080/documentation/knob",
#             "http://localhost:8080/documentation/color_input",
#             "http://localhost:8080/documentation/color_picker",
#             "http://localhost:8080/documentation/date",
#             "http://localhost:8080/documentation/time",
#             "http://localhost:8080/documentation/upload",
#             "http://localhost:8080/documentation/teleport",
#             "http://localhost:8080/documentation/interactive_image",
#             "http://localhost:8080/documentation/audio",
#             "http://localhost:8080/documentation/video",
#             "http://localhost:8080/documentation/icon",
#             "http://localhost:8080/documentation/avatar",
#             "http://localhost:8080/documentation/table",
#             "http://localhost:8080/documentation/aggrid",
#             "http://localhost:8080/documentation/echart",
#             "http://localhost:8080/documentation/pyplot",
#             "http://localhost:8080/documentation/matplotlib",
#             "http://localhost:8080/documentation/line_plot",
#             "http://localhost:8080/documentation/plotly",
#             "http://localhost:8080/documentation/linear_progress",
#             "http://localhost:8080/documentation/circular_progress",
#             "http://localhost:8080/documentation/spinner",
#             "http://localhost:8080/documentation/scene",
#             "http://localhost:8080/documentation/leaflet",
#             "http://localhost:8080/documentation/tree",
#             "http://localhost:8080/documentation/log",
#             "http://localhost:8080/documentation/editor",
#             "http://localhost:8080/documentation/code",
#             "http://localhost:8080/documentation/json_editor",
#             "http://localhost:8080/documentation/storage",
#             "http://localhost:8080/documentation/page",
#             "http://localhost:8080/documentation/card",
#             "http://localhost:8080/documentation/column",
#             "http://localhost:8080/documentation/row",
#             "http://localhost:8080/documentation/grid",
#             "http://localhost:8080/documentation/list",
#             "http://localhost:8080/documentation/expansion",
#             "http://localhost:8080/documentation/scroll_area",
#             "http://localhost:8080/documentation/separator",
#             "http://localhost:8080/documentation/space",
#             "http://localhost:8080/documentation/skeleton",
#             "http://localhost:8080/documentation/splitter",
#             "http://localhost:8080/documentation/tabs",
#             "http://localhost:8080/documentation/stepper",
#             "http://localhost:8080/documentation/timeline",
#             "http://localhost:8080/documentation/carousel",
#             "http://localhost:8080/documentation/pagination",
#             "http://localhost:8080/documentation/menu",
#             "http://localhost:8080/documentation/context_menu",
#             "http://localhost:8080/documentation/tooltip",
#             "http://localhost:8080/documentation/notify",
#             "http://localhost:8080/documentation/notification",
#             "http://localhost:8080/documentation/dialog",
#             "http://localhost:8080/documentation/query",
#             "http://localhost:8080/documentation/colors",
#             "http://localhost:8080/documentation/dark_mode",
#             "http://localhost:8080/documentation/add_style",
#             "http://localhost:8080/documentation/timer",
#             "http://localhost:8080/documentation/keyboard",
#             "http://localhost:8080/documentation/refreshable",
#             "http://localhost:8080/documentation/generic_events",
#             "http://localhost:8080/documentation/run_javascript",
#             "http://localhost:8080/documentation/clipboard",
#             "http://localhost:8080/documentation/page_layout",
#             "http://localhost:8080/documentation/page_title",
#             "http://localhost:8080/documentation/navigate",
#             "http://localhost:8080/documentation/download",
#             "http://localhost:8080/documentation/run",
#         ]

#         for url in urls:
#             add_page_to_pdf(page, url, pdf_writer)
#             time.sleep(0.5)  # slow down to avoid errors on localhost:8080

#         browser.close()

#         # Add the final "The End" page
#         add_end_page(pdf_writer)

#         with open(output_path, 'wb') as output_pdf:
#             pdf_writer.write(output_pdf)

# if __name__ == "__main__":
#     import time
#     start_time = time.time()

#     pdf_file = 'zzz9_merged_output.pdf'
#     generate_pdf(pdf_file)

#     overall_time = time.time() - start_time
#     print(f"Crawling time: {overall_time:.2f} sec.s to create {pdf_file}")



from playwright.sync_api import sync_playwright
import io
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

MAX_PAGE_HEIGHT_MM = 5080  # Maximum height per ISO 32000 standard

def get_page_height(page, url):
    page.goto(url)
    height_px = page.evaluate("document.body.scrollHeight")
    # height_mm = height_px * 0.264583  # convert pixels to millimeters
    height_mm = round(height_px * 0.264583, 2)  # convert pixels to millimeters and round to 2 decimal places
    print(f"{height_mm}mm = {url}")
    # Smallest Value
    #     203.2mm for the URL: http://localhost:8080/documentation/page_title
    # Average Value
    #     2558.05mm (calculated by summing all heights and dividing by the number of entries)
    # Largest Value
    #     8854.27mm for the URL: http://localhost:8080/documentation/page_layout
    return height_mm

def add_page_to_pdf(page, url, pdf_writer):
    # print(url)
    page.goto(url)
    page.emulate_media(media="screen")

    height_mm = get_page_height(page, url)
    if height_mm > MAX_PAGE_HEIGHT_MM:
        height_mm = MAX_PAGE_HEIGHT_MM

    pdf_buffer = page.pdf(
        width='210mm',  # standard A4 width
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

        # List of local URLs to scrape and convert to PDF
        urls = [
            "http://localhost:8080/documentation/",
            "http://localhost:8080/documentation/section_text_elements",
            "http://localhost:8080/documentation/section_controls",
            "http://localhost:8080/documentation/section_audiovisual_elements",
            "http://localhost:8080/documentation/section_data_elements",
            "http://localhost:8080/documentation/section_binding_properties",
            "http://localhost:8080/documentation/section_page_layout",
            "http://localhost:8080/documentation/section_styling_appearance",
            "http://localhost:8080/documentation/section_action_events",
            "http://localhost:8080/documentation/section_pages_routing",
            "http://localhost:8080/documentation/section_configuration_deployment",
            "http://localhost:8080/documentation/label",
            "http://localhost:8080/documentation/link",
            "http://localhost:8080/documentation/chat_message",
            "http://localhost:8080/documentation/element",
            "http://localhost:8080/documentation/markdown",
            "http://localhost:8080/documentation/restructured_text",
            "http://localhost:8080/documentation/mermaid",
            "http://localhost:8080/documentation/html",
            "http://localhost:8080/documentation/image",
            "http://localhost:8080/documentation/button",
            "http://localhost:8080/documentation/button_group",
            "http://localhost:8080/documentation/button_dropdown",
            "http://localhost:8080/documentation/badge",
            "http://localhost:8080/documentation/chip",
            "http://localhost:8080/documentation/toggle",
            "http://localhost:8080/documentation/radio",
            "http://localhost:8080/documentation/select",
            "http://localhost:8080/documentation/checkbox",
            "http://localhost:8080/documentation/switch",
            "http://localhost:8080/documentation/slider",
            "http://localhost:8080/documentation/range",
            "http://localhost:8080/documentation/joystick",
            "http://localhost:8080/documentation/input",
            "http://localhost:8080/documentation/textarea",
            "http://localhost:8080/documentation/codemirror",
            "http://localhost:8080/documentation/number",
            "http://localhost:8080/documentation/knob",
            "http://localhost:8080/documentation/color_input",
            "http://localhost:8080/documentation/color_picker",
            "http://localhost:8080/documentation/date",
            "http://localhost:8080/documentation/time",
            "http://localhost:8080/documentation/upload",
            "http://localhost:8080/documentation/teleport",
            "http://localhost:8080/documentation/interactive_image",
            "http://localhost:8080/documentation/audio",
            "http://localhost:8080/documentation/video",
            "http://localhost:8080/documentation/icon",
            "http://localhost:8080/documentation/avatar",
            "http://localhost:8080/documentation/table",
            "http://localhost:8080/documentation/aggrid",
            "http://localhost:8080/documentation/echart",
            "http://localhost:8080/documentation/pyplot",
            "http://localhost:8080/documentation/matplotlib",
            "http://localhost:8080/documentation/line_plot",
            "http://localhost:8080/documentation/plotly",
            "http://localhost:8080/documentation/linear_progress",
            "http://localhost:8080/documentation/circular_progress",
            "http://localhost:8080/documentation/spinner",
            "http://localhost:8080/documentation/scene",
            "http://localhost:8080/documentation/leaflet",
            "http://localhost:8080/documentation/tree",
            "http://localhost:8080/documentation/log",
            "http://localhost:8080/documentation/editor",
            "http://localhost:8080/documentation/code",
            "http://localhost:8080/documentation/json_editor",
            "http://localhost:8080/documentation/storage",
            "http://localhost:8080/documentation/page",
            "http://localhost:8080/documentation/card",
            "http://localhost:8080/documentation/column",
            "http://localhost:8080/documentation/row",
            "http://localhost:8080/documentation/grid",
            "http://localhost:8080/documentation/list",
            "http://localhost:8080/documentation/expansion",
            "http://localhost:8080/documentation/scroll_area",
            "http://localhost:8080/documentation/separator",
            "http://localhost:8080/documentation/space",
            "http://localhost:8080/documentation/skeleton",
            "http://localhost:8080/documentation/splitter",
            "http://localhost:8080/documentation/tabs",
            "http://localhost:8080/documentation/stepper",
            "http://localhost:8080/documentation/timeline",
            "http://localhost:8080/documentation/carousel",
            "http://localhost:8080/documentation/pagination",
            "http://localhost:8080/documentation/menu",
            "http://localhost:8080/documentation/context_menu",
            "http://localhost:8080/documentation/tooltip",
            "http://localhost:8080/documentation/notify",
            "http://localhost:8080/documentation/notification",
            "http://localhost:8080/documentation/dialog",
            "http://localhost:8080/documentation/query",
            "http://localhost:8080/documentation/colors",
            "http://localhost:8080/documentation/dark_mode",
            "http://localhost:8080/documentation/add_style",
            "http://localhost:8080/documentation/timer",
            "http://localhost:8080/documentation/keyboard",
            "http://localhost:8080/documentation/refreshable",
            "http://localhost:8080/documentation/generic_events",
            "http://localhost:8080/documentation/run_javascript",
            "http://localhost:8080/documentation/clipboard",
            "http://localhost:8080/documentation/page_layout",
            "http://localhost:8080/documentation/page_title",
            "http://localhost:8080/documentation/navigate",
            "http://localhost:8080/documentation/download",
            "http://localhost:8080/documentation/run",
        ]

        for url in urls:
            add_page_to_pdf(page, url, pdf_writer)
            time.sleep(0.5)  # slow down to avoid errors on localhost:8080

        browser.close()

        # Add the final "The End" page
        add_end_page(pdf_writer)

        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    import time
    start_time = time.time()

    pdf_file = 'zzz9_merged_output.pdf'
    generate_pdf(pdf_file)

    overall_time = time.time() - start_time
    print(f"Crawling time: {overall_time:.2f} sec.s to create {pdf_file}")





# from playwright.sync_api import sync_playwright

# def get_page_height(page, url):
#     page.goto(url)
#     height = page.evaluate("document.body.scrollHeight")
#     return height

# def find_page_heights():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch()
#         page = browser.new_page()

#         # List of local URLs to scrape
#         urls = [
#             "http://localhost:8080/documentation/",
#             "http://localhost:8080/documentation/section_text_elements",
#             "http://localhost:8080/documentation/section_controls",
#             "http://localhost:8080/documentation/section_audiovisual_elements",
#             "http://localhost:8080/documentation/section_data_elements",
#             "http://localhost:8080/documentation/section_binding_properties",
#             "http://localhost:8080/documentation/section_page_layout",
#             "http://localhost:8080/documentation/section_styling_appearance",
#             "http://localhost:8080/documentation/section_action_events",
#             "http://localhost:8080/documentation/section_pages_routing",
#             "http://localhost:8080/documentation/section_configuration_deployment",
#             "http://localhost:8080/documentation/label",
#             "http://localhost:8080/documentation/link",
#             "http://localhost:8080/documentation/chat_message",
#             "http://localhost:8080/documentation/element",
#             "http://localhost:8080/documentation/markdown",
#             "http://localhost:8080/documentation/restructured_text",
#             "http://localhost:8080/documentation/mermaid",
#             "http://localhost:8080/documentation/html",
#             "http://localhost:8080/documentation/image",
#             "http://localhost:8080/documentation/button",
#             "http://localhost:8080/documentation/button_group",
#             "http://localhost:8080/documentation/button_dropdown",
#             "http://localhost:8080/documentation/badge",
#             "http://localhost:8080/documentation/chip",
#             "http://localhost:8080/documentation/toggle",
#             "http://localhost:8080/documentation/radio",
#             "http://localhost:8080/documentation/select",
#             "http://localhost:8080/documentation/checkbox",
#             "http://localhost:8080/documentation/switch",
#             "http://localhost:8080/documentation/slider",
#             "http://localhost:8080/documentation/range",
#             "http://localhost:8080/documentation/joystick",
#             "http://localhost:8080/documentation/input",
#             "http://localhost:8080/documentation/textarea",
#             "http://localhost:8080/documentation/codemirror",
#             "http://localhost:8080/documentation/number",
#             "http://localhost:8080/documentation/knob",
#             "http://localhost:8080/documentation/color_input",
#             "http://localhost:8080/documentation/color_picker",
#             "http://localhost:8080/documentation/date",
#             "http://localhost:8080/documentation/time",
#             "http://localhost:8080/documentation/upload",
#             "http://localhost:8080/documentation/teleport",
#             "http://localhost:8080/documentation/interactive_image",
#             "http://localhost:8080/documentation/audio",
#             "http://localhost:8080/documentation/video",
#             "http://localhost:8080/documentation/icon",
#             "http://localhost:8080/documentation/avatar",
#             "http://localhost:8080/documentation/table",
#             "http://localhost:8080/documentation/aggrid",
#             "http://localhost:8080/documentation/echart",
#             "http://localhost:8080/documentation/pyplot",
#             "http://localhost:8080/documentation/matplotlib",
#             "http://localhost:8080/documentation/line_plot",
#             "http://localhost:8080/documentation/plotly",
#             "http://localhost:8080/documentation/linear_progress",
#             "http://localhost:8080/documentation/circular_progress",
#             "http://localhost:8080/documentation/spinner",
#             "http://localhost:8080/documentation/scene",
#             "http://localhost:8080/documentation/leaflet",
#             "http://localhost:8080/documentation/tree",
#             "http://localhost:8080/documentation/log",
#             "http://localhost:8080/documentation/editor",
#             "http://localhost:8080/documentation/code",
#             "http://localhost:8080/documentation/json_editor",
#             "http://localhost:8080/documentation/storage",
#             "http://localhost:8080/documentation/page",
#             "http://localhost:8080/documentation/card",
#             "http://localhost:8080/documentation/column",
#             "http://localhost:8080/documentation/row",
#             "http://localhost:8080/documentation/grid",
#             "http://localhost:8080/documentation/list",
#             "http://localhost:8080/documentation/expansion",
#             "http://localhost:8080/documentation/scroll_area",
#             "http://localhost:8080/documentation/separator",
#             "http://localhost:8080/documentation/space",
#             "http://localhost:8080/documentation/skeleton",
#             "http://localhost:8080/documentation/splitter",
#             "http://localhost:8080/documentation/tabs",
#             "http://localhost:8080/documentation/stepper",
#             "http://localhost:8080/documentation/timeline",
#             "http://localhost:8080/documentation/carousel",
#             "http://localhost:8080/documentation/pagination",
#             "http://localhost:8080/documentation/menu",
#             "http://localhost:8080/documentation/context_menu",
#             "http://localhost:8080/documentation/tooltip",
#             "http://localhost:8080/documentation/notify",
#             "http://localhost:8080/documentation/notification",
#             "http://localhost:8080/documentation/dialog",
#             "http://localhost:8080/documentation/query",
#             "http://localhost:8080/documentation/colors",
#             "http://localhost:8080/documentation/dark_mode",
#             "http://localhost:8080/documentation/add_style",
#             "http://localhost:8080/documentation/timer",
#             "http://localhost:8080/documentation/keyboard",
#             "http://localhost:8080/documentation/refreshable",
#             "http://localhost:8080/documentation/generic_events",
#             "http://localhost:8080/documentation/run_javascript",
#             "http://localhost:8080/documentation/clipboard",
#             "http://localhost:8080/documentation/page_layout",
#             "http://localhost:8080/documentation/page_title",
#             "http://localhost:8080/documentation/navigate",
#             "http://localhost:8080/documentation/download",
#             "http://localhost:8080/documentation/run",
#         ]

#         for url in urls:
#             height_px = get_page_height(page, url)
#             height_mm = height_px * 0.264583
#             print(f"Height of {url}: {height_px}px ({height_mm:.2f}mm)")

#         browser.close()

# if __name__ == "__main__":
#     import time
#     start_time = time.time()    

#     find_page_heights()

#     overall_time = time.time() - start_time
#     print(f"Total crawling time: {overall_time:.2f} seconds")


