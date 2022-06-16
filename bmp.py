
import numpy as np
import skimage.io
import struct
import os.path
import matplotlib.image as mpimg

# BMP class
class BMP:

    def __init__(self, path):
        self.__path = path
        bmp = open(path, "rb")

        self.tof = bmp.read(2)
        if self.tof != b'BM':
            self.__correct_type = False
        else:
            self.__correct_type = True
        
        

        # Getting the offset postion 10 -> 4 reads
        bmp.seek(10, 0)
        self.__offset = struct.unpack('I', bmp.read(4))[0]

        # Get the height & width  : postion 18,22 -> 4 reads
        bmp.seek(18, 0)
        self.__width = struct.unpack('I', bmp.read(4))[0]
        self.__height = struct.unpack('I', bmp.read(4))[0]

         # Get bits per pixel : position 28 -> 2 reads 
        bmp.seek(28, 0)
        self.__bits_per_pixel = struct.unpack('H', bmp.read(2))[0]

        # Get compression : position 30 -> 4 reads 
        bmp.seek(30, 0)
        self.__compression = struct.unpack('I', bmp.read(4))[0]


    def __repr__(self) -> str:
        res = "File info:" + '\n'
        res += 'file: ' +  str(self.__path) + '\n'
        res += 'type:' + str(self.tof) + '\n'
        res += 'offset: ' + str(self.__offset) + '\n'
        res += 'width: ' + str(self.__width) + '\n'
        res += 'height: ' + str(self.__height) + '\n'
        res += 'bits per pixel: ' + str(self.__bits_per_pixel) + '\n'
        res += 'compression type: ' + str(self.__compression) + '\n'
        return res

    # Accessor Methods
    def get_path(self):
        """ return path."""
        return self.__path

    def get_offset(self):
        """ return offset."""
        return self.__offset

    def get_width(self):
        """ return width. """
        return self.__width

    def get_height(self):
        """ return coupon rate. """
        return self.__height
    
    def get_bits_per_pixel(self):
        """ return bits per pixel. """
        return self.__bits_per_pixel
    
    def get_compression(self):
        """ return compression type. """
        return self.__compression

    def get_correct_type(self):
        """ returns if correct type"""
        return self.__correct_type

    def read_rows(self):
        """ reads each row of the pixel array and builds and array of the image's pixels"""
        image_file = open(self.get_path(), "rb")
        # skip the BMP header.
        image_file.seek(self.get_offset())

        # We need to read pixels in as rows to later swap the order
        # since BMP stores pixels starting at the bottom left.
        rows = []
        row = []
        pixel_index = 0
        
        width = self.get_width()
        height = self.get_height()
        while True:
            if pixel_index == width:
                pixel_index = 0
                rows.insert(0, row)
                if len(row) != width * 3:
                    raise Exception("Row length is not " + str(width) + "*3 but " + str(len(row)) + " / 3.0 = " + str(len(row) / 3.0))
                row = []
            pixel_index += 1

            r_string = image_file.read(1)
            g_string = image_file.read(1)
            b_string = image_file.read(1)
            
        
        
            if len(r_string) == 0:
                # This is expected to happen when we've read everything.
                if len(rows) != height:
                    print("Warning!!! Read to the end of the file at the correct sub-pixel (red) but we've not read" + str(height) + " rows!")
                break

            if len(g_string) == 0:
                print("Warning!!! Got 0 length string for green. Breaking.")
                # raise ValueError
                break

            if len(b_string) == 0:
                
                print("Warning!!! Got 0 length string for blue. Breaking.")
                raise ValueError
                break

            r = ord(r_string)
            g = ord(g_string)
            b = ord(b_string)

            row.append(b)
            row.append(g)
            row.append(r)

        image_file.close()

        self.rows = rows
    

    def repack_sub_pixels(self):
        """ packs all the sub_pixels into one numpy array"""
        print("Repacking pixels...")
        width = self.get_width()
        height = self.get_height()
        sub_pixels = []
        for row in self.rows:
            for sub_pixel in row:
                sub_pixels.append(sub_pixel)

        diff = len(sub_pixels) - height * width * 3
        print("Packed", len(sub_pixels), "sub-pixels.")
        if diff != 0:
            print("Error! Number of sub-pixels packed does not match " + str(width) + "*" + str(height) + "*3 = "  + str(width * height * 3) + " : (" + str(len(sub_pixels)) + " - " + str(width) + " * " + str(height) + " * 3 = " + str(diff) +").")
            
        self.pixels = np.array(sub_pixels, dtype=np.uint8)
        
    def negate_pixels(self):
        """ converts pixels to its negative """
        image = np.reshape(self.pixels, (self.get_height(), self.get_width(),3))
        neg = 255 - image
        self.neg_pixels = neg

    def fail_safe_negate_and_read(self):
        """ failsafe if above doesn't work"""
        image = mpimg.imread(self.get_path())
        neg = 255 - image
        self.neg_pixels = neg

    def parse_filename(self):
        """ parses for the file name """
        path = os.path.splitext(self.get_path())[0]
        self.file_name = os.path.basename(path)
    
    def export_image(self):
        """ exports the image to .bmp with a new name"""
        self.parse_filename()
        new_file_name = str(self.file_name + "_negative.bmp")
        skimage.io.imsave(fname = new_file_name, arr = self.neg_pixels)


#####################################################################
### unit test code:
if __name__ == "__main__":
    path = 'Sample Images/bmp_24.bmp'
    image = BMP(path)
    print(image)
    # print(image.check_bmp())
    # print(image.get_offset())
    # print(image.get_width(), image.get_height())
    # print(image.get_bits_per_pixel())
    # print(image.get_compression())
    # print(image.get_correct_type())
    try:
        image.read_rows()
        image.repack_sub_pixels()
        image.negate_pixels()

    except:
        print('Using fail_safe method instead')
        image.fail_safe_negate_and_read()
       
    print(image.rows)
    print()
    print(image.pixels)
    
    
    # image.export_image()