import sys
import struct

file_name = "MARBLES"
print(file_name)

with open(f'{file_name}.bmp','rb') as bmp:
    byte = bmp.read(1)
    while byte:
        print(byte)
        bmp.read(1)