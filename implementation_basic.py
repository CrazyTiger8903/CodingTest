"""
구현 : 머리속에 있는 알고리즘을 소스코드로 바꾸는 과정
1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
2. 실수 연산을 다루고, 특성 소수점 자리까지 출력해야 하는 문제
3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
4. 적절한 라이브러리를 찾아서 사용해야 하는 문제
"""

"""
2차원 공간에서의 방향 벡터

동 북 서 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]
"""

# 1. 상하좌우 문제

# N = int(input())
# list = input().split()

# x, y = 1, 1

# dir = ['L', 'R', 'U', 'D']

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for i in list:
#     for j in range(len(dir)):
#         if i == dir[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]
#     if nx < 1 or ny <1 or nx > N or ny > N:
#         continue

#     x = nx
#     y = ny

# print(x, y)

# 2번 시각

# N = int(input())

# count = 0

# for i in range(N+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count+=1

# print(count)

# 3번 왕실의 나이트

# data = input()
# x = int(data[1])
# y = int(ord(data[0])) - int(ord('a')) + 1

# dirs = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# count = 0

# for dir in dirs:
#     nx = x + dir[0]
#     ny = y + dir[1]
#     if nx >= 1 and nx <= 8 and ny >=1 and ny <=8:
#         count+=1

# print(count)

# 4번 문자열 재정렬

S = input()
result = []
value = 0

for i in S:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))