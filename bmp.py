
import numpy as np
import skimage.io
import struct

# BMP class
class BMP:

    def __init__(self, path):
        self.__path = path
        bmp = open(path, "rb")

        # Getting the offset postion 10 -> 4 reads
        bmp.seek(10, 0)
        self.__offset = struct.unpack('I', bmp.read(4))[0]

        # Get the height & width  : postion 18,22 -> 4 reads
        bmp.seek(18, 0)
        self.__width = struct.unpack('I', bmp.read(4))[0]
        self.__height = struct.unpack('I', bmp.read(4))[0]

    def __repr__(self) -> str:
        res = 'file: ' +  str(self.__path) + '\n'
        res += 'offset: ' + str(self.__offset) + '\n'
        res += 'width: ' + str(self.__width) + '\n'
        res += 'height: ' + str(self.__height) + '\n'
        return res
        

#####################################################################
### unit test code:
if __name__ == "__main__":
    path = 'clue.bmp'
    image = BMP(path)
    print(image)