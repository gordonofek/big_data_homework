#!/usr/bin/env python
"""reducer.py"""
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    results = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            results.append((current_word, total_count))
        except ValueError:
            pass

    # Sort by count descending and take only the top 3
    top_3 = sorted(results, key=itemgetter(1), reverse=True)[:3]
    for word, count in top_3:
        print('%s%s%d' % (word, separator, count))

if __name__ == "__main__":
    main()