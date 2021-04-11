# input()을 통해 문자열을 받고 이를 split()하여 각각의 원소로 나누고 숫자 자료형으로 변환후, list화
x = list(map(int, input().split()))

result = sum([7, 3, 5, 2])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4]) # 오름차순
print(result) # 1, 4, 5, 8, 9
result = sorted([9, 1, 8, 5, 4], reverse=True) # 내림차순
print(result) # 9, 8, 5, 4, 1

# 자료형을 리스트나 튜플로 한 경우
result = sorted([("홍길동", 35), ("이순신", 75), ("아무개", 50)], key = lambda x: x[1], reverse=True)
print(result) # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]

data = [9, 1, 8, 5, 4]
data.sort()
print(data)


from itertools import permutations

data = ["A", "B", "C"] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기

print(result)
# [("A", "B", "C"), ("A", "C", "B"), ("B", "A", "C"), ("B", "C", "A"), ("C", "A", "B"), ("C", "B", "A")]


from itertools import combinations

data = ["A", "B", "C"] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C)]


from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복허용)

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4

from bisect import bisect_left, bisect_right


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))  # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))  # 6

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) # 리스트 자료형으로 변환

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # 사전 자료형으로 변환
'''
{'red': 2, 'blue': 3, 'green': 1}
'''

import math

print(math.factorial(5)) # 120

print(math.sqrt(7)) # 2.6457513110645907

print(math.gcd(21, 14)) # 7

print(math.pi) # 3.141592653589793

print(math.e) # 2.718281828459045