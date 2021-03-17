'''
- https://programmers.co.kr/learn/courses/30/lessons/12945

# [풀이과정]
    - 첫번째 풀이는 답은 맞지만 테스트 런타임 에러 및 시간 초과 발생 
    - 케이스 갯수가 많아지면서 func(n-1)+func(n-2) 역으로 추적하기에 시간이 초과되서 일까?
    - 숫자가 커지니 속도가 현저히 느려지긴 하네, 
    - 그렇다면, 나눴을 때의 규칙이 있는지 확인해보자. 없다.
    - 이전의 값을 저장해놔야 하는 형태로 해야할것 같다. 리스트를 써보자. 
'''

'''
# [첫번째 풀이]
def func(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    return func(n-1) + func(n-2)

def solution(n):
    return func(n) % 1234567
'''


# [두번째 풀이]
def solution(n) :
    # fibo =[0, 1]
    fibo = [0] * (n+1) # 길이만큼 선언해줘야 index out of range 에러 발생 않음
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n] % 1234567

print(solution(3))
print(solution(5))

# [다른 사람 풀이1]
def fibonacci1(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b,a+b
    return a

# [다른 사람 풀이2]
def fibonacci2(num):
    answer = [0,1]
    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    #print(answer)
    return answer[-1]

# print(fibonacci1(3))
# print(fibonacci1(5))