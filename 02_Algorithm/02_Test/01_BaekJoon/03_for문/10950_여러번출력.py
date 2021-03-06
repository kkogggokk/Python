'''
- https://www.acmicpc.net/problem/10950
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''

case = int(input())
tmp = list() # store input values in tmp

for _ in range(case):
    A, B = map(int, input().split())
    tmp.append(A)
    tmp.append(B)

for i in range(0, len(tmp), 2):
    print(tmp[i] + tmp[i + 1])


