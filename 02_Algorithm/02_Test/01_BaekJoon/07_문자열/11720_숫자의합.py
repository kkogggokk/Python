'''
- https://www.acmicpc.net/problem/11720
N개의 숫자가 공백 없이 쓰여있다. 
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
N개의 숫자가 공백 없이 쓰여있다. 
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

- [변수]
    - n : N개의 숫자 입력 (int) 
    - value : n자리수 만큼 입력 

- [질문]
    - 두번째 입력받을 때 n자리수 만큼 입력받으려면 입력받은 다음에 입력값 제한을 하는거니까 입력할 때 갯수 제한을 둘수는 없는거지?
- [hint]
    - 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.
'''

n = int(input()) 
result = list()

while True : 
    value = input()
    if n == len(value):
        for i in value : 
            result.append(int(i))
        print(sum(result))
        break
    else : 
        print('입력 값에 맞춰 입력해주세요.')

