import requests
import xml.etree.ElementTree as ET

def fetch_and_parse_sitemap(sitemap_url="https://ifindcheaters.com/sitemap.xml"):
    response = requests.get(sitemap_url)
    urls_with_expected_data = {}

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for url_element in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
            loc = url_element.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            urls_with_expected_data[loc] = {
                "title": "Expected Title for " + loc,
                "description": "Expected Description for " + loc,
            }
    else:
        print(f"Failed to fetch sitemap: {response.status_code}")

    return urls_with_expected_data
