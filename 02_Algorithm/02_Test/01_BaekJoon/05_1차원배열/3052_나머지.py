'''
- https://www.acmicpc.net/problem/3052

- 입력 10개를 받는다. 
- 42로 나눈 나머지 값들을 리스트로 저장한다. 
- 리스트 값들 유니크 값 확인 => 셋 -> 카운트 
'''
lst = list()

for i in range(10) : 
    num = int(input())
    lst.append(num%42)

print(len(set(lst)))

