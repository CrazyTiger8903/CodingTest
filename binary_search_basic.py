"""
순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방식
이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

동작 과정 :
1. 시작점, 끝점, 중간점
2. 중간점 비교
3. 새로운 시작점 또는 끝점 선택 및 중간점 선택
4. 반복

시간복잡도 : O(logN)
"""
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
    
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소 없음")
# else:
#     print(result+1)


# 파이썬 이진 탐색 라이브러리
# bisect_left : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
# bisect_right와 bisect_left의 값을 빼주면 값이 특정 범위에 속하는 데이터 개수를 구할 수 있다.

# from bisect import bisect_left, bisect_right

# a = [1,2,4,4,8]
# x = 4

# # 결과 : 2, 4
# print(bisect_left(a, x))
# print(bisect_right(a, x))


# 파라메트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법 -> 이진탐색을 이용하여 해결 가능

# 1번 : 떡볶이 떡 만들기
# n, m = map(int, input().split())
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0
# while(start<=end):
#     total = 0
#     mid = (start+end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid
#     if total < m:
#         end = mid -1
#     else:
#         result = mid
#         start = mid +1

# print(result)

# 2번: 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
array = list(map(int, input().split()))

right = bisect_right(array, m)
left = bisect_left(array, m)

print(right - left)