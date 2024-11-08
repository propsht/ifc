import xml.etree.ElementTree as ET
import json

# Parse the sitemap.xml file to extract URLs
def parse_sitemap(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract URLs from the sitemap
    urls = []
    for url in root.findall(".//url/loc"):
        urls.append(url.text)

    return urls

# Save the extracted URLs to a JSON file
def save_urls_to_json(urls, output_file='sitemap_urls.json'):
    data = {"urls": urls}
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    # Specify the path to your sitemap.xml file
    sitemap_file = 'sitemap.xml'

    # Parse the sitemap and get URLs
    urls = parse_sitemap(sitemap_file)

    # Save the URLs to a JSON file
    save_urls_to_json(urls)

if __name__ == "__main__":
    main()
