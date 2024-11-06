import json
import requests
from bs4 import BeautifulSoup


# Fetch sitemap URLs from the given sitemap URL
def fetch_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        urls = [url_loc.text for url_loc in soup.find_all('loc')]
        return urls
    else:
        print(f"Failed to fetch sitemap: {response.status_code}")
        return []


# Save URLs to a JSON file
def save_urls_to_json(urls, file_path="sitemap_urls.json"):
    with open(file_path, "w") as f:
        json.dump({"urls": urls}, f, indent=4)
    print(f"Sitemap URLs saved to {file_path}")


# Main function
def main():
    sitemap_url = "https://ifindcheaters.com/sitemap.xml"
    urls = fetch_sitemap_urls(sitemap_url)

    if urls:
        save_urls_to_json(urls)
    else:
        print("No URLs found in the sitemap.")


if __name__ == "__main__":
    main()
