# collections 라이브러리의 Counter는 등장회수를 세는 기능
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # 사전 자료형으로 변환