import time
from collections import deque
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

base_url = "http://localhost:8080/documentation/"

def gather_urls(page, base_url, visited):
    # print(f"Gathering URLs from: {page.url}")
    elements = page.query_selector_all("a")
    urls = []
    base_domain = urlparse(base_url).netloc

    for element in elements:
        href = element.get_attribute("href")
        if href:
            # Create a full URL and parse it
            full_url = urljoin(base_url, href)
            parsed_url = urlparse(full_url)
            
            # Check if the URL is from the same domain, not visited, and does not contain a fragment
            if parsed_url.netloc == base_domain and parsed_url.fragment == '' and full_url not in visited and full_url not in urls:
                urls.append(full_url)
                # print(f"Valid URL added: {full_url}")

    return urls

def get_all_urls():
    visited = set()  # Using set for visited to efficiently check for membership
    all_urls = []    # Using list to maintain order of all URLs found
    to_visit = deque([base_url])  # Using deque for efficient stack operations

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # page.set_default_navigation_timeout(10000)

        while to_visit:
            current_url = to_visit.pop()  # Efficient pop from the right side (stack behavior)
            # print(f"\nVisiting: {current_url}")
            if current_url not in visited:
                page.goto(current_url)
                time.sleep(0.2) # well, FastAPI isn't fast enough ... need LudicrousSpeedAPI
                visited.add(current_url)
                new_urls = gather_urls(page, base_url, visited)

                # Append new URLs to all_urls if they are not already present
                for url in new_urls:
                    if url not in all_urls:
                        all_urls.append(url)

                # Extend to_visit with new URLs that have not been visited or scheduled for visit
                # Adding to the left side for these new URLs to be visited last
                for url in reversed(new_urls):
                    if url not in visited and url not in to_visit:
                        to_visit.append(url)  # Append to the right side for stack behavior

                # print(f"New URLs to visit: {len(new_urls)}")
                # for url in new_urls:
                #     print(f"\t{url}")

        browser.close()

    return all_urls


if __name__ == "__main__":
    import time

    start_time = time.time()
    to_crawl = get_all_urls()
    overall_time = time.time() - start_time
    print(f"Total crawling time: {overall_time:.2f} seconds")

    unique_urls = []
    excluded_urls = {"http://localhost:8080/", "http://localhost:8080/documentation"}
    mandatory_url = "http://localhost:8080/documentation/"

    # Ensure mandatory_url is at the top of the list
    unique_urls.append(mandatory_url)

    for url in to_crawl:
        if url not in unique_urls and url not in excluded_urls and url.startswith("http://localhost:8080/documentation/"):
            unique_urls.append(url)

    print(f"Total URLs found: {len(unique_urls)}")
    for url in unique_urls:
        print(url)

    with open("urls_to_crawl.txt", "w") as file:
        for url in unique_urls:
            file.write(url + "\n")


# Note: there is access to the registry at:
#   http://127.0.0.1:8080/static/search_index.json
# but that's a huge list of urls with anchor links similar to this:
#   274. Title: ui.scene: 3D Scene
#        URL: /documentation/scene#3d_scene
# which means that the huge list has lots of repeated pages with the same info, and so just different 
# spots on the same page ... which makes using Playwright a better solution (just slower) than:
# 
# import httpx
# url = 'http://localhost:8080/static/search_index.json'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     for i, item in enumerate(data, 1):
#         print(f"{i}. Title: {item['title']}")
#         print(f"   URL: {item['url']}")
#         print()
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")


