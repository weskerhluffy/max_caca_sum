#!/usr/bin/python3
'''
Created on Nov 18, 2018

@author: ernesto
'''

if __name__ == '__main__':
    a_tam = int(input())
    a = [int(x) for x in input().strip().split(" ")]
    r = [0] * a_tam
    r[0] = a[0]
    if a_tam > 1:
        r[1] = max(r[0], a[1])
    
    for i in range(2, a_tam):
        n = a[i]
        r[i] = max(r[i - 1], r[i - 2] + n, n)
    print(r[a_tam - 1])
