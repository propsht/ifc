import json

def save_parsed_data(url, title, description, filename="parsed_data.json"):
    try:
        # Load existing data if available
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Update data with new entry
    data[url] = {"title": title, "description": description}

    # Save data back to file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Saved parsed data for {url}")
