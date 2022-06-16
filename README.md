# BMP Photo Negative Generator

This program is a tool that can create the photo negative from an image stored in the [BMP File Format](https://en.wikipedia.org/wiki/BMP_file_format) and output the negative in BMP format. 

The user can pass in the path of a file with the following restrictions:
1. No compression was used on the image
2. Bits per pixel = 24
3. Is a Bitmap Image file (.bmp)

If the file does not meet these requirements, the program will display the appropriate error message and ask the user to input the path of a valid file. 

The BMP image will parse the raw metadata and build the photo negative from the file's Pixel array and export the negative in BMP format in the same directory as the program. 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

```python
python3 main.py
```