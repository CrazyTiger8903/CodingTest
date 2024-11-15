"""
그리디 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법
"""

# 1번 거스름돈
# 가장 큰 화폐 단위부터 돈을 거슬러 주면 됨
"""
n = int(input())
count = 0

list = [500, 100, 50, 10]

for i in list:
    count += n // i
    n %= i

print(count)
"""

# 2번: 1이 될 때까지

# n, k = map(int, input().split())
# count = 0

# while(n>1):
#     if n % k != 0:
#         n -= 1
#         count += 1
#     else:
#         n /= k
#         count += 1

# while True:
#     target = (n//k)*k
#     count += (n-target)
#     n = target

#     if n<k:
#         break

#     count +=1
#     n //= k

# count += (n-1)

# print(count)

# 3번: 곱하기 혹은 더하기

# data = input()

# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <=1:
#         result += num
#     else:
#         result *= num

# print(result)   

# 4번 : 모험가 길드

n = int(input())

data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count+=1
    if count >= i:
        result +=1
        count = 0

print(result)