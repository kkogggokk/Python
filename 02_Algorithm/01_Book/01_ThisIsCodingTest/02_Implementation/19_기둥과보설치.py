# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def possible(answer) :
    for x, y, stuff in answer :
        if stuff == 0 : # 기둥 설치할 경우
           # ** 바닥 위 | 보의 한쪽 끝부분 위 | 다른 기둥 위 => 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer :
                continue
            return False # 아니라면 거짓 반환

        elif stuff == 1 : # 보를 설치 할 경우
           # ** 한쪽 끝부분이 기 위 | 양쪽 끝부분이 다른 보와 동시에 연결 => 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
                continue
            return False둥
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame : # 작업의 개수는 최대 1000개
        x, y, stuff, operate = frame # 한 프레임에 있는 값을 x, y, stuff, operate에 할당

        if operate == 0 : # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제 한 뒤
            if not possible(answer) : # 만약 가능한 구조물 이라면
                answer.append([x, y, stuff]) # 다시 설치 한다.

        if operate == 1 : # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치 한 뒤
            if not possible(answer) : # 만약 설치 불가 구조물 이라면
                answer.remove([x, y, stuff]) # 다시 제거 한다.

    return sorted(answer)


n1, n2 = 5, 5
build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


print(solution(n1, build_frame1))
print(solution(n2, build_frame2))

# result 1 = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0], [5,1,0]]
# result 2 = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]



