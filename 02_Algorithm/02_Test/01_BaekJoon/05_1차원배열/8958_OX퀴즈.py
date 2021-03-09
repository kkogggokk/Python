'''
- https://www.acmicpc.net/problem/8958

- 변수 
    - num : 테스트 케이스의 갯수  
    - test_case : 각 테스트 케이스
        - list
        - 문자 , 각 문자 개별적으로 저장
    - check : 연속된 0의 갯수 확인
        - 초기값 = 0 
        - 'O' 만남 -> check += 1
        - 'X' 만남 -> check = 0 (reset)
    - score : check한 결과 담기 
        - list
        - check 한 값을 append
        - sum해서 출력 
'''
check = 0
score = list()

num = int(input())
for i in range(num) :
    test_case = list(input())

    while True : # 테스트 케이스 'O', 'X' 
        for i in range(len(test_case)) : 
            if test_case[i] == 'O' :
                check += 1
                score.append(check)
            elif test_case[i] == 'X' :
                check = 0
        print(sum(score))
        break
    check = 0 # reset안해서 결과값이 잘못 나왔음
    score.clear() # 끝나고 난 다음에 새로 받기 위해서 reset



