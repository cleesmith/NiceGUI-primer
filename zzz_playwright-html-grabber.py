from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup, NavigableString, Tag
import os

def extract_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html_content = page.content()
        browser.close()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
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
    filtered_text = filter_lines(plain_text, ignore_strings)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{'_'*60}\n")
        f.write(f"URL: {url}\n")
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
    urls_to_crawl = [
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
    
    ignore_strings = [
        "NiceGUI",
        "circle circle circle",
        "main.py",
        "See more...",
        "Connection lost. Trying to reconnect...",
        "prevent Prettier from removing this line",
    ]
    
    output_filename = "zzz9_crawled_pages.txt"
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
