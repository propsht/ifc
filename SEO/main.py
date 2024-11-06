from sitemap_parser import fetch_and_parse_sitemap
from page_verifier import verify_page

def verify_pages(urls_with_expected_data):
    for url, expected_data in urls_with_expected_data.items():
        print(f"Verifying {url}")
        verify_page(url, expected_data["title"], expected_data["description"])

if __name__ == "__main__":
    urls_with_expected_data = fetch_and_parse_sitemap()
    verify_pages(urls_with_expected_data)


