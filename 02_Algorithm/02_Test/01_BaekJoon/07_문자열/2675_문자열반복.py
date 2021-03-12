'''
- https://www.acmicpc.net/problem/2675 

- [변수]
    - T : 테스트 케이스 
    - R : 반복횟수 
    - S : 초기 입력받은 문자열
    - P : 초기 입력받은 문자열을 반복해서 나온 문자열 

'''

n = int(input())
P = ''

for i in range(n):
    R, S = input().split()
    for i in range(len(S)):
        P += S[i] * int(R)
    print(P)
    P = '' # 초기화 해줘야 다시 반복할때 새로운 값으로 

