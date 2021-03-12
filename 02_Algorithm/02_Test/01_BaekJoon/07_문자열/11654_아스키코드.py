'''
- https://www.acmicpc.net/problem/11654 
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
- ASCII 코드로 변환
    - ord(문자)
    - chr(숫자)
'''

value = input()
try : #문자가 들어 왔을 때 
    print(ord(value))
except TypeError: # 숫자일때 예외처리
    print(chr(int(value)))