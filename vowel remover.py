#! /usr/bin/env python

text = raw_input("Enter a word: ")

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print anti_vowel(text)
