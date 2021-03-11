'''
- https://www.acmicpc.net/problem/2577
'''

A = int(input())
B = int(input())
C = int(input())

num = A * B * C 
lst = list(str(num))

for i in range(10) :
    print(lst.count(str(i)))