# https://www.acmicpc.net/problem/9498

score = int(input())
if (0 <= score) and (score <= 100) :
    if (90 <= score) and (score <= 100) : # A : 90 - 100
        print('A')
    elif (80 <= score) and (score <= 89) : # B : 80 - 89
        print('B')
    elif (70 <= score) and (score <= 79) : # C : 70 - 79
        print('C')
    elif (60 <= score) and (score <= 69) : # D : 60 - 69
        print('D')
    else : # F : 60 미만
        print('F')