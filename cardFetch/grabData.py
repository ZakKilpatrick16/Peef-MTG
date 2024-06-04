import requests
import os

# Function to download a file
def download_file(url, directory="."):
    print(url)
    filename = os.path.join(directory, url.split("/")[-1])  # Extract filename from URL
    print(filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Create directory if it doesn't exist
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"File downloaded: {filename}")

# Get the Bulk Data endpoint URL
bulk_data_url = "https://api.scryfall.com/bulk-data"

# Make a request to get the list of available bulk data files
response = requests.get(bulk_data_url)
if response.status_code == 200:
    bulk_data = response.json()

    # Iterate over the bulk data files
    for data_file in bulk_data['data']:
        download_url = data_file['download_uri']
        download_file(download_url, "./bulkFiles/")  # Change "downloads" to the directory where you want to save the files
else:
    print("Failed to fetch bulk data files.")
