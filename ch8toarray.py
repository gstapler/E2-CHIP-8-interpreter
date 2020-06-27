#!/usr/bin/env python
from sys import argv

# USAGE: >python ch8toarray.py [chip8 ROM filename]
# Output can be routed to a text file via: python ch8toarray.py [ROM filename] >> output.txt

filename = argv[1]
idx = 512

with open(filename, 'rb') as f:
    byte = f.read(1)
    while byte:
        print("Memory[0x" + str(hex(program_start_address + idx)).upper()[2:] + ", number] = 0x", end = '')
        print(byte.hex().upper(), end='\n')
        byte = f.read(1)
        idx += 1