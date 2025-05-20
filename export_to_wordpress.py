import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime



# WordPress API credentials
WP_URL = "https://pbochenski.pl/wp-json/wp/v2"
WP_USER = "admin2519"
#WP_PASS = "OxxN 6SfN FoeI 87li I2EW luuX"
WP_PASS = "vV0WL%!Io$BXcmSk&!C2"
auth = HTTPBasicAuth(WP_USER, WP_PASS)

# Path to the folder containing images
IMAGE_FOLDER = "/Users/pawel/Documents/kod/pbochenski.github.io/media/large"
METADATA_FOLDER = "/Users/pawel/Documents/kod/pbochenski.github.io/_gallery"

def upload_image(image_path, data):
    with open(image_path, 'rb') as img_file:
        file_name = os.path.basename(image_path)
        

        data = {
            "title": data['title'],
            "alt_text": data['title'],
            "caption": f"{data['title']}, {data['date']}",
            "description": data['title'],
            "date": data['formatted_date'],
        }
        print(data)

        # Upload the image
        print(f"Uploading {file_name} \n")
        response = requests.post(
            f"{WP_URL}/media",
            auth=auth,
            data=data,
            files={'file': img_file}
        )
        if response.status_code == 201:
            return response.json().get('id')
        else:
            print(f"Failed to upload {file_name}: {response.status_code} - {response.text}")
            return None

def create_post(image_id, metadata):
    
    data = {
        'title': metadata['title'],
        'status': 'publish',
        'featured_media': image_id,
        'categories': [2],
        'date': metadata['formatted_date'],
    }

    print(f"Creating post with data: {data} \n")
    response = requests.post(
        f"{WP_URL}/posts",
        data=data,
        auth=auth
    )
    if response.status_code == 201:
        print(f"Post created: {response.json().get('link')}")
    else:
        print(f"Failed to create post: {response.status_code} - {response.text}")

def extract_metadata(file_path):
    # Extract metadata from corresponding .md file
        metadata_file = os.path.join(
            METADATA_FOLDER, 
            f"{os.path.splitext(os.path.basename(file_path))[0]}.md"
        )
        data = {
            'id': "",
            'date': "",
            'title': "",
            'formated_date': "",
        }
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as meta_file:
                for line in meta_file:
                    if line.startswith("name:"):
                        data['title'] = line.split(":", 1)[1].strip()
                    elif line.startswith("date:"):
                        data['date'] = line.split(":", 1)[1].strip()
                    elif line.startswith("filename:"):
                        data['id'] = line.split(":", 1)[1].strip().removesuffix(".jpg")
        
        data['formatted_date'] = datetime.strptime(data['date'], "%Y.%m.%d").strftime("%Y-%m-%dT%H:%M:%S")
        return data

def main():
    for file_name in sorted(os.listdir(IMAGE_FOLDER)):
        if file_name.lower().endswith(('.jpg')):
            image_path = os.path.join(IMAGE_FOLDER, file_name)
            data = extract_metadata(file_name)
            print(f"Processing {file_name} with metadata: {data}")
            image_id = upload_image(image_path, data)
            if image_id:
                create_post(image_id, data)

if __name__ == "__main__":
    main()