import json
from playwright.sync_api import sync_playwright
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load URLs from the sitemap_urls.json file
with open('sitemap_urls.json', 'r') as file:
    data = json.load(file)
    urls = data['urls']

# Function to initialize Playwright and run the title, description, and h1 verification
def verify_title_description_h1(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)

            # Get the title, description, and h1
            title = page.title()
            description = page.locator('meta[name="description"]').get_attribute('content')
            h1 = page.locator('h1').inner_text()

            # Log the results
            logger.info(f"URL: {url}")
            logger.info(f"Title: {title}")
            logger.info(f"Description: {description}")
            logger.info(f"H1: {h1}")

            # Save results to a dictionary
            page_data = {
                'url': url,
                'title': title,
                'description': description,
                'h1': h1
            }

            # Write results to page_data.json
            with open('page_data.json', 'a') as json_file:
                json.dump(page_data, json_file, indent=4)
                json_file.write(",\n")  # Ensure commas separate entries for easier parsing later

            # Close the browser
            browser.close()

    except Exception as e:
        logger.error(f"Error occurred while processing {url}: {e}")

# Main function to iterate over URLs and call the verify function
def main():
    for url in urls:
        verify_title_description_h1(url)
        time.sleep(2)  # Delay to avoid hitting the server too fast

if __name__ == "__main__":
    main()
