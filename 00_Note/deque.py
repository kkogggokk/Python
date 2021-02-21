# cellections 라이브러리 기능 중 dequde 클래스
# popleft()     : 첫번째 원소 제거
# pop()         : 마지막 원소 제거
# appendleft(x) : 첫번째 인덱스에 원소 x 삽입
# append(x)     : 마지막 인덱스에 원소 x 삽입

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
