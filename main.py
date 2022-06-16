
from bmp import * 


def main():
    while True:
        try:
            path = str(input("Enter .bmp image file path: ")) 
            if os.path.exists(path):
                print("File found")
                image = BMP(path)
                if image.get_correct_type() == False:
                    print("Wrong file type. Please enter the path of a .bmp file.")
                if image.get_compression() != 0:
                    print("Compression detected. Please choose a non-compressed .bmp file.")
                if image.get_bits_per_pixel() != 24:
                    print("Invalid bits per pixel. Please choose a .bmp with 24 bits per pixel.")
                else:
                    break;
                    
            else:
                print("File not found. Please enter a valid file path")      
        except ValueError:
            print("Invalid")
        continue
    
   
    try:
        image.read_rows()
        image.repack_sub_pixels()
        image.negate_pixels()

    except:
        print('Using fail_safe method instead')
        image.fail_safe_negate_and_read()

    image.export_image()
    print('Image exported as:', image.file_name + "_negative.bmp")
    
if __name__ == "__main__":
    main()
