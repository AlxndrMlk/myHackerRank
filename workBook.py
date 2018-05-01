#!/bin/python3

import sys

def slicer(a, k):  
    
    """
    a = no. of problems / chapter
    k = no. of problems / page
    """
    
    sliced = []
    
    for i, step in enumerate(range(0, a, k)):
        sliced.append([x for x in range(a)][step:k*i+k])
    
    return sliced


def matcher(n, k, a):    

    """
    n = no. of chapters
    a = no. of problems / chapter
    k = no. of problems / page
    """
    work_book = []
    matches = 0

    for i in range(n):
        work_book += slicer(a[i], k)
        
    for i, page in enumerate(work_book):
        if i in page:
            matches += 1
    
    return matches


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = list(map(int, input().strip().split(' ')))
    result = matcher(n, k, a)
    print(result)
