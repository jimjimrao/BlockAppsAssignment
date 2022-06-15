import sys
import struct
import numpy as np
import skimage.io

file_name = "clue"
print(file_name)

with open(f'{file_name}.bmp', 'rb') as bmp:

    # Getting the offset postion 10 -> 4 reads
    bmp.seek(10, 0)
    offset = struct.unpack('I', bmp.read(4))[0]

    # Get the height & width  : postion 18,22 -> 4 reads
    bmp.seek(18, 0)
    bmp_w = struct.unpack('I', bmp.read(4))[0]
    bmp_h = struct.unpack('I', bmp.read(4))[0]

    print(bmp_h, bmp_w)

# Get the size  : postion 34 -> 4 reads
    bmp.seek(34, 0)
    bmp_s = struct.unpack('I', bmp.read(4))[0]


# Getting the number of bytes in a row
    bmp_b = int(bmp_s/bmp_h)
    print(bmp_h, bmp_w, bmp_s, bmp_b)
# 3-  Reading Data from the Picture
    bmp.seek(offset, 0)

    bmp_line = ''
    bmp_list = []
    bmp_list_v = []

    for line in range(bmp_h):
        for byte in range(bmp_b):
#             print('pixel:',line,byte)
            temp = []
            bmp_byte = bmp.read(1)
            for i in range(3):
                temp.append(struct.unpack('B', bmp_byte)[0])
#             print(temp)
            bmp_list.append(temp)
        bmp_list_v.append(bmp_list)
        bmp_list = []
   
    # bmp_list_v.reverse()
    bmp_list_v = np.array(bmp_list_v)
    print(bmp_list_v)
    print(bmp_list_v.shape)
    # for line in bmp_list_v:
    #     print(line)

    skimage.io.imsave(fname="result2.bmp", arr=bmp_list_v)
