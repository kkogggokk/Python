'''
- https://www.acmicpc.net/problem/10951
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
각 테스트 케이스마다 A+B를 출력한다.

- 빠져나오는 조건이 없는데? 조건식이 없는 while문?
- EOF
- while을 먼저하는거 vs try를 먼저하는거?
'''

try:
    while True:
        num1, num2 = map(int, input().split())
        print(num1 + num2)
except:
    exit()