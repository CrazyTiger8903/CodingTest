"""
다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
주로 탑다운 방식과 바텀업 방식 존재

조건1 : 최적 부분 구조 - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결
조건2 : 중복되는 부분 문제 - 동일한 작은 문제를 반복적으로 해결

예시1) 피보나치 수열
점화식 : 인접한 항들 사이의 관계식
-> 재귀함수 - 중복되는 부분 문제(f2가 여러 번 호출) -> 시간이 너무 오래걸림
조건 1, 조건 2 만족 -> DP 사용

하향식(탑다운) - 메모이제이션
한번 계산한 결과를 메모리 공간에 메모하는 기법(캐싱)
주로 하향식(탑다운) 사용 - 결과 저장용 리스트는 DP 테이블 이라고 부름

상향식(바텀업)
작은 문제들 부터 큰 문제 순서대로 차례대로 계산
"""

# 탑다운(하향식) - 메모이제이션 / 피보나치 수열

# 메모이제이션을 위한 DP 테이블
# d = [0] * 100

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
    
#     if d[x] != 0:
#         return d[x]
    
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99))

# 바텀업(상향식)
# d = [0] * 100

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]

# print(d[n])

"""
다이나믹 프로그래밍 vs 분할정복
둘다 최적 부분 구조를 가질 때 사용할 수 있다.
하지만 다이나믹 프로그래밍은 부분 문제의 중복을 포함한다.
ex) 퀵 정렬 - 분할 정복 : 분할 이후에 피벗은 다른 부분 문제에 호출되지 않는다
"""

# 문제 1 : 개미전사
# (i-1)과 (i-2)+(i) 2가지 경우 비교

# n = int(input())
# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = array[1]

# for i in range(2,n):
#     d[i] = max(d[i-1], d[i-2]+array[i])

# print(d[n-1])

# 문제 2 : 1로 만들기

# x = int(input())

# d = [0]*10000

# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)    

# print(d[x])

# 문제 3 : 효율적인 화폐 구성

# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))

# d = [10001] * (m+1)

# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m+1):
#         if d[j - array[i]] != 10001:
#             d[j] = min(d[j], d[j-array[i]]+1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

# 문제 4 : 금광
# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     array = list(map(int, input().split()))
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index += m
#     for j in range(1,m):
#         for i in range(n):
#             if i == 0: left_up = 0
#             else: left_up = dp[i-1][j-1]
#             if i == n -1: left_down = 0
#             else: left_down = dp[i+1][j-1]
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left, left_down, left_up)
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m-1])
#     print(result)


# 문제 5 : 병사 배치하기
# 최장 증가 부분 수열

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))