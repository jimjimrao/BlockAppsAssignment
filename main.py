
from bmp import * 


def main():
    while True:
        try:
            path = str(input("Enter .bmp image file path: ")) 
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
