#! /usr/bin/env python

import sys

k, p = map(int, sys.stdin.readline().split())
scores=[]

for i in xrange(k):
    data = sys.stdin.readline().split()
    score = int(data[0])*(i+1)
    scores.append((score, k-i, data[1]))

scores.sort(reverse=True)

for i in xrange(p):
    print scores[i][2]
