# BMP Photo Negative Generator

This program is a tool that can create the photo negative from an image stored in the [BMP File Format](https://en.wikipedia.org/wiki/BMP_file_format) and output the negative in BMP format. 

The user can pass in the path of a file with the following restrictions:
1. No compression was used on the image
2. Bits per pixel = 24
3. Is a Bitmap Image file (.bmp)

If the file does not meet these requirements, the program will display the appropriate error message and ask the user to input the path of a valid file. 

The BMP image will parse the raw metadata and build the photo negative from the file's Pixel array and export the negative in BMP format in the same directory as the program. 

Some examples of invalid and working BMP image files are provided in the [Images Folder](https://github.com/jimjimrao/BlockAppsAssignment/tree/main/Images)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```
```console
Enter .bmp image file path or type '--help' for instructions: sample.bmp
File found 

File info:
file: sample.bmp
type:b'BM'
offset: 138
width: 640
height: 426
bits per pixel: 24
compression type: 0
 

Repacking pixels...
Packed 817920 sub-pixels.
Creating negative...

Negative exported as: sample_negative.bmp in the same directory as this program
```

Original File: sample.bmp
![Alt text](https://raw.githubusercontent.com/jimjimrao/BlockAppsAssignment/main/Images/sample.bmp?token=GHSAT0AAAAAABT4NFNHE4CAVZDQMQPCBWQYYVLNP5Q "a title")

Exported photo negative: sample_negative.bmp
![Alt text](https://raw.githubusercontent.com/jimjimrao/BlockAppsAssignment/main/Images/sample_negative.bmp?token=GHSAT0AAAAAABT4NFNHYS5V5KBNPAR2ZJ6OYVLNQGA "a title")

