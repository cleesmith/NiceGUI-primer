from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, NavigableString, Tag
import os

SECTIONS = 0

def extract_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html_content = page.content()
        browser.close()

    soup = BeautifulSoup(html_content, 'html.parser')

    # remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    def extract_text_from_element(element):
        text = []
        if isinstance(element, Tag):
            if element.name == 'table':
                text.append("\n")
                for row in element.find_all('tr'):
                    row_text = []
                    for cell in row.find_all(['td', 'th']):
                        cell_text = cell.get_text().strip()
                        row_text.append(cell_text)
                    text.append(' '.join(row_text))
                return '\n'.join(text)
            elif element.name == 'pre':
                # Mark <pre> tags distinctly
                text.append(f"[nicegui-pre]{element.get_text()}[/nicegui-pre]")
            else:
                for child in element.children:
                    if isinstance(child, NavigableString):
                        text.append(child.strip())
                    elif child.name in ['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
                        text.append('\n' + extract_text_from_element(child))
                    else:
                        text.append(extract_text_from_element(child))
        return ' '.join(filter(None, text))

    plain_text = extract_text_from_element(soup.body)
    return plain_text

def filter_lines(text, ignore_strings):
    lines = text.split('\n')
    filtered_lines = []
    blank_line_count = 0
    in_pre_block = False
    
    for line in lines:
        line = line.rstrip().removesuffix(" link")
        if "[nicegui-pre]" in line:
            in_pre_block = True
            line = "Coding example:\n" + line.split("[nicegui-pre]", 1)[-1]
        
        if "[/nicegui-pre]" in line:
            line = line.split("[/nicegui-pre]", 1)[0]
            in_pre_block = False

        if any(line.strip().startswith(ignore_str) for ignore_str in ignore_strings):
            continue
        
        if line.strip() == '':
            blank_line_count += 1
        else:
            blank_line_count = 0
        
        if blank_line_count < 3:
            filtered_lines.append(line)
    
    return '\n'.join(filtered_lines)

def append_to_file(filename, url, plain_text, ignore_strings):
    global SECTIONS
    filtered_text = filter_lines(plain_text, ignore_strings)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{'_'*60}\n")
        SECTIONS += 1
        f.write(f"Section: {SECTIONS}. URL: {url}\n")
        f.write(filtered_text)
        f.write("\n\n")  # Add extra newlines for separation between pages

def process_urls(urls, ignore_strings, output_filename):
    for i, url in enumerate(urls, 1):
        try:
            print(f"Processing URL {i} of {len(urls)}: {url}")
            plain_text = extract_text(url)
            append_to_file(output_filename, url, plain_text, ignore_strings)
            print(f"Appended content from {url} to {output_filename}")
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

if __name__ == "__main__":
    urls_to_crawl = []
    with open("urls_to_crawl.txt", "r") as file:
        # read all lines from the file and strip any leading/trailing whitespace
        urls_to_crawl = [line.strip() for line in file]
    
    ignore_strings = [
        "NiceGUI",
        "circle circle circle",
        "main.py",
        "See more...",
        "Connection lost. Trying to reconnect...",
        "prevent Prettier from removing this line",
        '?xml version="1.0" encoding="UTF-8"?',
        "dark_mode light_mode brightness_auto",
        "more_vert",
        "If you like NiceGUI, go and become a",
    ]
    
    output_filename = "nicegui_docs.txt"
    import os
    if os.path.exists(output_filename):
        os.remove(output_filename)
    print(f"Removed existing file: {output_filename}")    

    import time
    start_time = time.time()    

    process_urls(urls_to_crawl, ignore_strings, output_filename)

    overall_time = time.time() - start_time
    print(f"Total crawling time: {overall_time:.2f} seconds")

    print(f"All processing complete. Output saved to {os.path.abspath(output_filename)}")
