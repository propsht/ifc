import json
import pytest

# Set the correct paths for the JSON files
actual_data_path = "/Users/propsht/Documents/QA/projects/ifc/SEO/page_data.json"
expected_data_path = "/Users/propsht/Documents/QA/projects/ifc/SEO/page_data_expect.json"

# Load the actual data from page_data.json
with open(actual_data_path, "r") as f:
    actual_data = json.load(f)

# Load the expected data from page_data_expect.json
with open(expected_data_path, "r") as f:
    expected_data = json.load(f)


@pytest.mark.parametrize("url", actual_data.keys())
def test_page_data(url):
    # Get the actual and expected data for the URL
    actual_entry = actual_data[url]
    expected_entry = expected_data[url]

    # Verify Title
    assert actual_entry["title"] == expected_entry["title"], f"Title mismatch for URL '{url}'."

    # Verify Description
    assert actual_entry["description"] == expected_entry["description"], f"Description mismatch for URL '{url}'."

    # Verify H1 Tag
    assert actual_entry["h1"] == expected_entry["h1"], f"H1 mismatch for URL '{url}'."
