from playwright.sync_api import sync_playwright
from data_storage import save_parsed_data

def verify_page(url, expected_title, expected_description):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url, timeout=30000)  # Extended timeout for slower pages

            # Wait until the title matches the expected title
            page.wait_for_function(f'document.title === "{expected_title}"', timeout=15000)

            # Extract the actual title and description
            actual_title = page.title()
            description_element = page.query_selector('meta[name="description"]')
            actual_description = description_element.get_attribute("content") if description_element else ""

            # Compare actual and expected values
            if actual_title == expected_title and actual_description == expected_description:
                print(f"{url} - Verification successful")
            else:
                print(f"{url} - Verification failed")
                print(f"Expected title: {expected_title}, Actual title: {actual_title}")
                print(f"Expected description: {expected_description}, Actual description: {actual_description}")

            # Save parsed data
            save_parsed_data(url, actual_title, actual_description)

        except Exception as e:
            print(f"An error occurred while verifying {url}: {e}")

        finally:
            browser.close()
