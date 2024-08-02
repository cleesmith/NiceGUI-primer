# # pip install playwright
# # playwright install
# import os
# import re
# from urllib.parse import urljoin, urlparse
# from collections import deque
# import html2text
# from playwright.sync_api import sync_playwright

# def scrape_nicegui_docs(base_url, output_dir):
#     visited_urls = set()
#     to_visit = deque([base_url])
#     print(f"to_visit: type={type(to_visit)}:\n{to_visit}")
#     total_pages = 0
#     scraped_pages = 0
#     h = html2text.HTML2Text()
#     h.ignore_links = False

#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)

#     def is_valid_url(url):
#         parsed_base = urlparse(base_url)
#         parsed_url = urlparse(url)
#         return (parsed_url.netloc == parsed_base.netloc and
#                 parsed_url.path.startswith(parsed_base.path))

#     def clean_text(text):
#         # Remove any remaining HTML tags
#         text = re.sub(r'<[^>]+>', '', text)
#         # Remove any potential JavaScript
#         text = re.sub(r'<script[\s\S]*?</script>', '', text)
#         # Remove any potential CSS
#         text = re.sub(r'<style[\s\S]*?</style>', '', text)
#         # Remove "Connection lost. Trying to reconnect..." text
#         text = text.replace('Connection lost. Trying to reconnect...', '')
#         return text

#     def save_content_as_text(url, content):
#         # Extract part of the URL after 'http://127.0.0.1:8080/'
#         parsed_url = urlparse(url)
#         path_after_base = parsed_url.path.lstrip('/')
#         filename = path_after_base.replace('/', '_') + '.txt'
#         filepath = os.path.join(output_dir, filename)
        
#         text_content = h.handle(str(content))
#         text_content = clean_text(text_content)
        
#         with open(filepath, 'w', encoding='utf-8') as f:
#             f.write(f"URL: {url}\n\n")
#             f.write(text_content)
        
#         print(f"Saved: {filepath}")
#         print(f"URL: {url}")  # Print the URL of the saved page

#     def scrape_page(url, page):
#         nonlocal total_pages, scraped_pages
        
#         print(f"\nScraping: {url}")  # Print the URL being scraped
#         scraped_pages += 1
        
#         try:
#             page.goto(url, timeout=10000)
#             page.wait_for_load_state('networkidle')
#         except Exception as e:
#             print(f"Failed to retrieve {url}. Error: {e}")
#             return
        
#         content = page.content()
        
#         save_content_as_text(url, content)
        
#         links = page.locator('a')
#         count = links.count()
#         for i in range(count):
#             link_url = links.nth(i).get_attribute('href')
#             # don't follow -> "href":"#
#             if link_url and not link_url.startswith('#'):
#                 full_url = urljoin(base_url, link_url)
#                 if is_valid_url(full_url) and full_url not in visited_urls:
#                     # print(f"\nis_valid_url:")
#                     # print(f"link_url: type={type(link_url)}:\n{link_url}")
#                     # print(f"full_url: type={type(full_url)}:\n{full_url}")
#                     to_visit.append(full_url)
#                     # print(f"to_visit: type={type(to_visit)}:\n{to_visit}")
#                     visited_urls.add(full_url)
#                     # print(f"visited_urls: type={type(visited_urls)}:\n{visited_urls}")
#                     total_pages += 1

#     # begin scraping:
#     print("begin scraping:")
#     total_pages += 1  # Count the initial page
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         while to_visit:
#             current_url = to_visit.popleft()
#             print(f"while to_visit: current_url: type={type(current_url)}:\n{current_url}")
#             scrape_page(current_url, page)
#             print(f"\n********************************************")
#             print(f"after scrape_page: Progress: {scraped_pages}/{total_pages} pages scraped")

#         browser.close()

#     print(f"\nScraping complete. Total pages scraped: {scraped_pages}")
#     print(f"Text files saved in: {output_dir}")

# # Usage
# base_url = "http://localhost:8080/documentation"
# output_dir = "nicegui_docs_text"
# scrape_nicegui_docs(base_url, output_dir)

# # http://localhost:8080/documentation/section_text_elements
# # http://localhost:8080/documentation/section_controls
# # http://localhost:8080/documentation/section_audiovisual_elements
# # http://localhost:8080/documentation/section_data_elements
# # http://localhost:8080/documentation/section_binding_properties
# # http://localhost:8080/documentation/section_page_layout
# # http://localhost:8080/documentation/section_styling_appearance
# # http://localhost:8080/documentation/section_action_events
# # http://localhost:8080/documentation/section_pages_routing
# # http://localhost:8080/documentation/section_configuration_deployment


# pip install playwright
# playwright install
import os
import re
from urllib.parse import urljoin, urlparse
from collections import deque
import html2text
from playwright.sync_api import sync_playwright

# Customize HTML2Text to include full URLs inline
class CustomHTML2Text(html2text.HTML2Text):
    print("CustomHTML2Text")
    def handle_a(self, href, title, text):
        print(href)
        return f'{text} ({href})'

def scrape_nicegui_docs(base_url, output_dir):
    visited_urls = set()
    to_visit = deque([
        "http://localhost:8080/documentation/section_text_elements",
        "http://localhost:8080/documentation/section_controls",
        "http://localhost:8080/documentation/section_audiovisual_elements",
        "http://localhost:8080/documentation/section_data_elements",
        "http://localhost:8080/documentation/section_binding_properties",
        "http://localhost:8080/documentation/section_page_layout",
        "http://localhost:8080/documentation/section_styling_appearance",
        "http://localhost:8080/documentation/section_action_events",
        "http://localhost:8080/documentation/section_pages_routing",
        "http://localhost:8080/documentation/section_configuration_deployment"
    ])
    print(f"to_visit: type={type(to_visit)}:\n{to_visit}")
    total_pages = 0
    scraped_pages = 0
    # h = html2text.HTML2Text()
    h = CustomHTML2Text()
    h.body_width = 70  # Prevent line wrapping
    h.mark_code = True  # Do not mark code blocks
    h.ignore_links = False
    h.inline_links = True

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    def clean_text(text):
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'<script[\s\S]*?</script>', '', text)
        text = re.sub(r'<style[\s\S]*?</style>', '', text)
        text = text.replace('Connection lost. Trying to reconnect...', '')
        text = text.replace('_circle_ _circle_ _circle_', '')
        text = text.replace('_link_', '')
        text = text.replace('_content_copy_', '')
        text = text.replace("main.py", '')
        text = text.replace('**', '')
        text = text.replace('---|---', '')
        text = text.replace(':|', ':')
        text = re.sub(r'\bNiceGUI\b', '', text)
        return text

    def save_content_as_text(url, content):
        # Extract part of the URL after 'http://127.0.0.1:8080/'
        parsed_url = urlparse(url)
        path_after_base = parsed_url.path.lstrip('/')
        filename = path_after_base.replace('/', '_') + '.txt'
        filepath = os.path.join(output_dir, filename)
        
        print(f"save_content_as_text:\n{str(content)}")
        text_content = h.handle(str(content))
        # text_content = clean_text(text_content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n\n")
            f.write(text_content)
        
        print(f"Saved: {filepath}")
        print(f"URL: {url}")  # Print the URL of the saved page

    def scrape_page(url, page):
        nonlocal total_pages, scraped_pages
        
        print(f"\nScraping: #{scraped_pages}. {url}")  # Print the URL being scraped
        scraped_pages += 1
        
        try:
            page.goto(url, timeout=5000)
            # page.wait_for_load_state('networkidle') # very slow!
            page.wait_for_load_state('domcontentloaded') # or 'load'
        except Exception as e:
            print(f"Failed to retrieve {url}. Error: {e}")
            return
        
        content = page.content()
        # print(f"page: type={type(page)}:\n{page.content}")
        
        save_content_as_text(url, content)

    # begin scraping:
    total_pages += len(to_visit)  # Count the initial list of pages
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        while to_visit:
            current_url = to_visit.popleft()
            scrape_page(current_url, page)
            break

        browser.close()

    print(f"\nScraping complete. Total pages scraped: {scraped_pages}")
    print(f"Text files saved in: {output_dir}")

# Usage
base_url = "http://localhost:8080/documentation"
output_dir = "nicegui_docs_text"
scrape_nicegui_docs(base_url, output_dir)
