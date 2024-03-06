

# def fetch_image_urls(query: str, max_links_to_fetch: int):
#     base = "https://www.google.com"
#     url = f"{base}/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}"
#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, 'html.parser')
#     image_elements = soup.find_all("img")

#     image_urls = []
#     for img in image_elements[:max_links_to_fetch]:
#         img_url = img["src"]
#         # Check if the URL is absolute
#         if img_url.startswith('http') or img_url.startswith('www'):
#             image_urls.append(img_url)
#         else:
#             # If not, make it absolute
#             image_urls.append(f"{base}{img_url}")

#     return image_urls


# # Example usage:
# image_urls = fetch_image_urls('Dorreswami', 5)




import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import urllib.request



import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from fastcore.foundation import L

def search_images(keywords, max_images = 15):
    print(f"Searching for {keywords}")
    return L(DDGS().images(keywords,max_results=max_images)).itemgot('image')
image_urls =search_images('Car',max_images=10)

print("Image links:")
for link in image_urls:
    print(link)









def detect_faces(image_urls):
    """Detects faces in the images located at the given URLs."""
    likely_human_urls = []

    for url in image_urls:
        # Send a GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Convert the response content into a numpy array
        img_array = np.array(bytearray(response.content), dtype=np.uint8)

        # Decode the image
        img = cv2.imdecode(img_array, -1)

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # If faces are found, it means there's likely a human in the image
        if len(faces) > 0:
            likely_human_urls.append(url)

    return likely_human_urls



# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Example usage:
likely_human_urls = detect_faces(image_urls)
print("The images with faces:\n")
print(len(image_urls))
for url in likely_human_urls:
    print(url)
