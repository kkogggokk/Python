'''
- https://www.acmicpc.net/problem/10952
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.
'''


''' 풀이 1 > 런타임 에러 발생 
lst = list()
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        for i in range(len(lst)):
            print(lst[i])
        break
    else:
        lst.append(num1+num2)
'''
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    print(num1 + num2)