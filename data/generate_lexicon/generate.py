#!/usr/bin/env python3
from num2words import num2words
import sys
sys.path.insert(1, './indic_num2words')
from num_to_word import num_to_word
print(num_to_word(23, 'hi'))
f = open("lexicon_words.txt", "a")
for number in range(1, 200):
    s = str(number) + " " + num_to_word(number, "hi") + "\n"
    f.write(s)    
    p = str(number) + " " + num_to_word(number, "en") + "\n"
    f.write(p)
f.close()
