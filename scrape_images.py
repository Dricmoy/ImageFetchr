import os
import requests
import json

# Replace with your actual Pixabay API key
API_KEY = '45195094-9233bb35bf21daff3fbc87bc2'
URL = 'https://pixabay.com/api/'

def fetch_images(query, num_images=10):
    params = {
        'key': API_KEY,
        'q': query,
        'image_type': 'photo',
        'per_page': num_images
    }
    response = requests.get(URL, params=params)
    data = response.json()
    image_urls = [hit['webformatURL'] for hit in data['hits']]
    
    return image_urls

if __name__ == '__main__':
    user_input = 'unique generated images'
    if os.path.exists('images.json'):
        os.remove('images.json')
    
    images = fetch_images(user_input, 9)  # Fetch 15 images related to 'ai'
    with open('images.json', 'w') as file:
        json.dump(images, file)
    
    print(f"Fetched {len(images)} images.")
