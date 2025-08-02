# Image CLI made with Python

## Features

Features:
- convert WEBP images into another format
- create a thumbnail of a picture

## Installation

It's recommended to use a Python virtual environment: `python -m venv venv`

Activation on Linux: `source venv/bin/activate`

Activation on Windows: `.\venv\Scripts\activate` (use `Set-ExecutionPolicy Unrestricted -Scope Process`)

Install dependencies: `pip install -r requirements.txt`


## Usage

Convert WEBP images: `python images.py convert-webp DIRECTORY FORMAT`

Example: `python images.py convert-webp images-to-convert png`

You can use option `--delete` to delete original pictures when converted.

---

Create a thumbnail: `python images.py thumbnail FILE WIDTH HEIGHT OUTPUT`

Example: `python images.py thumbnail picture.jpg 450 600 picture-thumbnail.jpg`

