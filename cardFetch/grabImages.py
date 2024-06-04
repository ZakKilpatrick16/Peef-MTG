import os
import requests
from dotenv import load_dotenv
from supabase import create_client
import json
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv('PROJECT_URL')
supabase_key = os.getenv('SECRET_KEY')
supabase = create_client(supabase_url, supabase_key)

# File containing image URLs
filepath = "./bulkFiles/unique-artwork-*.json"

# Read the file and extract the image URLs
with open(filepath, 'r') as file:
    data = json.load(file)
    image_urls = []

    for entry in data:
        if 'image_uris' in entry and 'large' in entry['image_uris']:
            image_urls.append(entry['image_uris']['large'])

# Upload and display the first four images from the URL list
for image_url in image_urls[:4]:
    # Download the image from the URL
    response = requests.get(image_url)
    
    if response.status_code == 200:

        image_content = response.content  # Get the binary content of the image

        # Extract image name from URL
        image_name = image_url.split('/')[-1]
        
        # Display the image using matplotlib
        # image = Image.open(BytesIO(image_content))
        # plt.imshow(image)
        # plt.title(image_name)
        # plt.axis('off')  # Hide axis
        # plt.show()

        
        # Upload the image to Supabase storage
        try:
            # Upload the image to Supabase storage
            upload_response = supabase.storage.from_("mtgImages").upload(file=image_content, path=f"mtgImages/{image_name}", file_options={"content-type": "image/jpeg"})
            if upload_response.status_code == 200:
                print(f"Image '{image_name}' uploaded to storage.")
            else:
                print(f"Failed to upload image '{image_name}' to storage.")
        except Exception as e:
            print(f"Error uploading image '{image_name}': {e}")
    else:
        print(f"Failed to download image from URL: {image_url}")