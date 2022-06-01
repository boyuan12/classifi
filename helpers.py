import urllib.request 
from PIL import Image 

def get_image_size(url):
    image = Image.open(urllib.request.urlopen(url)) 
    width, height = image.size 
    return width, height
