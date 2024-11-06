import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse

# Function to parse a single page and extract title and description
async def parse_page(page, url):
    try:
        print(f"Parsing {url}")
        # Navigate to the page
        await page.goto(url)

        # Wait for the <h1> selector to be visible
        await page.wait_for_selector('h1', timeout=10000)  # Increased timeout

        # Extract the title and description
        title = await page.title()
        description = await page.query_selector('meta[name="description"]')

        # Get the content of the description meta tag, if available
        if description:
            description_content = await description.get_attribute('content')
        else:
            description_content = "No description available"

        print(f"Title: {title}")
        print(f"Description: {description_content}")
    except Exception as e:
        print(f"Failed to parse {url}: {str(e)}")

# Function to parse multiple pages
async def parse_pages(urls):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in urls:
            await parse_page(page, url)

        await browser.close()

# List of URLs to be parsed
urls = [
    'https://ifindcheaters.com',
    'https://ifindcheaters.com/blog/',
    'https://ifindcheaters.com/disclaimer/'
]

# Start parsing the pages
asyncio.run(parse_pages(urls))
