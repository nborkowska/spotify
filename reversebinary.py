#! /usr/bin/env python

import sys

def reverse(n):
    return int(bin(n)[2:][::-1], 2) 

data = sys.stdin.readline()
print reverse(int(data))


