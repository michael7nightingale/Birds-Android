"""
File for loading encoded handlers file `handlers.py` byte string.
It`s the place Simple UI takes handlers from.
"""
from base64 import b64encode

with open("handlers.py", 'rb') as file:
    print(b64encode(file.read()))
