#!/bin/bash

nasm -f elf -o teste.o teste.asm
gcc -m32 -no-pie -o teste teste.o
./teste