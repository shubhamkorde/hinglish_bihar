#!/usr/bin/env python3 
from num2words import num2words
import indic
A = []
file1 = open("words.txt","w")

for i in range(1000):
    s = str(i) + " " + num2words(i) + "\n"
    file1.write(s)
file1.close()