import requests
import xml.etree.ElementTree as ET
import json  # Import json for dumping the data to a file


# Function to fetch and parse the sitemap.xml
def fetch_sitemap(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch sitemap from {url}")
        return None


# Function to parse the sitemap.xml and extract URLs
def parse_sitemap(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    # Namespace handling for parsing the XML
    namespaces = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    urls = []
    for url in root.findall('url', namespaces):
        loc = url.find('loc', namespaces)
        if loc is not None:
            urls.append(loc.text)

    return urls


# Main function to fetch and save sitemap URLs as JSON
def main():
    sitemap_url = "https://ifindcheaters.com/sitemap.xml"
    print("Fetching sitemap...")
    xml_data = fetch_sitemap(sitemap_url)

    if xml_data:
        print("Parsing sitemap...")
        urls = parse_sitemap(xml_data)

        # Saving the URLs to a JSON file
        with open('sitemap_urls.json', 'w') as file:
            json.dump({"urls": urls}, file, indent=4)
        print(f"Saved {len(urls)} URLs to sitemap_urls.json")


if __name__ == "__main__":
    main()
