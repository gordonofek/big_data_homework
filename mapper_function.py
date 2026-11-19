#!/usr/bin/env python
"""mapper.py"""
import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # Strip trailing commas/dots and convert to lowercase
            clean_word = word.rstrip(',.').lower()
            if clean_word:
                print('%s%s%d' % (clean_word, separator, 1))

if __name__ == "__main__":
    main()