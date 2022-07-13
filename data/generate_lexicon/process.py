#!/usr/bin/env python3
import sys
sys.path.insert(1, './indic_num2words')
from num_to_word import num_to_word
def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

f = open("text.txt", "r")
words = set([])

lines = f.readlines()
for s in lines:
    for word in s.split():
        for subwords in word.split('.'):
            words.add(subwords)

words = sorted(words)
file = open("all_lexicon_words.txt", "a")

for word in words:
    if is_float(word):
        line = word + " " + num_to_word(int(word), 'hi')+"\n"
        file.write(line)    
        line2 = word + " " + num_to_word(int(word), 'en')+"\n"
        file.write(line2)
    else:
        line = word + " " + "\n"
        file.write(line)