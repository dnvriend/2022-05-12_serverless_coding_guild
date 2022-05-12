#!/usr/bin/env python
from PIL import Image

def show_image() -> None:
    image = Image.open('cat.jpg')
    image.show()

def thumbnail_image() -> None:
    image = Image.open('cat.jpg')
    image.thumbnail((400, 400))
    image.save('cat_thumbnail.jpg')

if __name__ == '__main__':
    thumbnail_image()