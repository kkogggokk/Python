'''
- https://www.acmicpc.net/problem/2439
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

- 왼쪽줄맞춤 : ljust()
- 가운데줄맞춤 : center()
- 오른쪽줄맞춤 : rjust()
- 오른쪽정렬하면서 0으로 채워주기 : zfill()
'''
num = int(input())

for i in range(1, num+1):
    str = '*' * i
    print(str.rjust(num))

