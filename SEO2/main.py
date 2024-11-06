import json
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests


# Step 1: Fetch sitemap URLs and save them to a JSON file
def fetch_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        urls = [url_loc.text for url_loc in soup.find_all('loc')]
        return urls
    else:
        print(f"Failed to fetch sitemap: {response.status_code}")
        return []


# Step 2: Parse each page's content (title, description, h1) and save immediately
async def parse_page_content(page, url):
    await page.goto(url)
    title = await page.title()
    description = await page.locator("meta[name='description']").get_attribute("content")

    # Disable strict mode for the `h1` locator to avoid errors with multiple h1 tags
    h1_locator = page.locator("h1", strict=False)
    h1 = await h1_locator.first.text_content() if await h1_locator.count() > 0 else ""

    return {
        "url": url,
        "title": title,
        "description": description if description else "",
        "h1": h1 if h1 else ""
    }


# Function to save data to a JSON file after each URL is parsed
def save_parsed_data(parsed_data, file_path="parsed_data.json"):
    with open(file_path, "a") as f:  # Open the file in append mode
        json.dump(parsed_data, f, indent=4)
        f.write("\n")  # Newline to separate entries for readability


# Main function to drive the process
async def main():
    sitemap_url = "https://ifindcheaters.com/sitemap.xml"
    urls = fetch_sitemap_urls(sitemap_url)

    # Step 1: Save URLs from sitemap to JSON
    save_parsed_data({"urls": urls}, "sitemap_urls.json")
    print(f"Sitemap URLs saved to sitemap_urls.json")

    # Step 2: Parse each URL and save results immediately
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for url in urls:
            print(f"Parsing {url}")
            try:
                page_data = await parse_page_content(page, url)
                save_parsed_data(page_data)
                print(f"Data for {url} saved.")
            except Exception as e:
                print(f"Failed to parse {url}: {e}")

        await browser.close()

    print("Parsing complete.")


# Run the main function
asyncio.run(main())
