#!/bin/python3

import os
#import numpy

# Complete the commonChild function below.
def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    m = [[0 for x in range(l2 + 1)] for y in range(l1 + 1)] 
    #m = numpy.zeros((l1 + 1, l2 + 1))
    for i in range(l1):
        for j in range(l2):
            if (s1[i] == s2[j]):
                m[i + 1][ j + 1] = m[i][j] + 1
            else:
                m[i + 1][ j + 1] = max(m[i + 1][j], m[i][ j + 1])

    return m[l1][l2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

