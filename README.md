# E2-CHIP-8-interpreter
# A CHIP-8 interpreter written for Expression 2 (E2), a scriptable entity from Wiremod, a mod for Garry's Mod

[CHIP-8](https://en.wikipedia.org/wiki/CHIP-8)
[Expression2](https://github.com/wiremod/wire/wiki/Expression-2)

## Overview

- Move chip8.txt and chip8_interpreter.txt and the contents of /includes/ (not the folder) to your Steam\steamapps\common\GarrysMod\data\expression2 folder.
- Use ch8toarray.py to convert CHIP-8 ROMs to E2 syntax. Copy and paste or route the output of the script to a text file and place it in your ...\GarrysMod\data\expression2 folder. Ignore the "Variable (Memory) does not exist" error.

1. chip8.txt is an example usage of the setup and usage of chip8_interpreter.txt.
2. chip8_interpreter.txt contains one function per instruction of the CHIP-8 interpreter. Each instruction is decoded inside of void step() by a switch case, which calls the corresponding function for any given instruction. Instructions EX9E, EXA1, FX07, and FX0A are unimplemented.
3. Included are a bunch of unconverted ROMs in /ROMs/. They do not have file headers, they are just a sequence of bytes.