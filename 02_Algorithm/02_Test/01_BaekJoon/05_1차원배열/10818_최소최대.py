'''
- https://www.acmicpc.net/problem/10818

- 변수 
    - n : 정수의 개수 
    - lst : n개 만큼 list에 

- n 입력 받았는데, lst입력 갯수 제한 둬야하지 않나?
'''

n = int(input())
lst = list(map(int,input().split()))
print(min(lst), max(lst))