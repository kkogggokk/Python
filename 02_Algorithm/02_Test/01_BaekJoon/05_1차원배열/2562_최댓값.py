'''
- https://www.acmicpc.net/problem/2562

'''
lst = list()

try :
    while True :
        num = int(input())
        lst.append(num)
except :
    print(max(lst))
    print(lst.index(max(lst))+1)
    exit()