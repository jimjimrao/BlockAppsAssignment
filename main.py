
from bmp import * 


def main():
    while True:
        try:
            path = str(input("Enter .bmp image file path or type '--help' for instructions: ")) 

            if path == "--help":
                print('\nUse this tool to get the photo negative of a .bmp image file. \n')
                print('Make sure your file has the following properties: \n \n     a. No compression was used on the image \n     b. Bits per pixel = 24 \n     c. Is a Bitmap Image file (.bmp)')

                print('\nOnce a valid file has been received by the program. A photo negative of \nthe image will be outputed in the same directory as this program in BMP format.')
            else:
                if os.path.exists(path):
                    print("File found \n")
                    image = BMP(path)
                    print(image,'\n')
                    if image.get_correct_type() == False:
                        print("Error: Wrong file type. Please enter the path of a .bmp file.")
                    if image.get_compression() != 0:
                        print("Error: Compression detected. Please choose a non-compressed .bmp file.")
                    if image.get_bits_per_pixel() != 24:
                        print("Error: Invalid bits per pixel. Please choose a .bmp file with 24 bits per pixel.")
                    else:
                        break;
                        
                else:
                    print("Error: File not found. Please enter a valid file path")      
        except ValueError:
            print("Invalid")

        print()
        continue
    
    # print(image)

    try:
        image.read_rows()
        image.repack_sub_pixels()
        image.negate_pixels()

    except:
        print('Manual parsing method failed. Using fail_safe method instead...')
        image.fail_safe_negate_and_read()

    print('Creating negative...\n')
    image.export_image()
    print('Negative exported as:', image.file_name + "_negative.bmp in the same directory as this program")

    

if __name__ == "__main__":
    main()
