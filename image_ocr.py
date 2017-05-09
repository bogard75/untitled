import sys
import requests
import pytesseract
from PIL import Image
from io import StringIO
from pytesseract import image_to_string

sys.stdout.write(pytesseract.image_to_string(image=Image.open('dddd.jpg'),lang='Kor'))