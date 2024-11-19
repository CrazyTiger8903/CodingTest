# 정렬 : 데이터를 특정 기준에 따라 순서대로 나열

# array = list(map(int, input().split()))

"""
선택정렬 : 뒤에서 선택해서 앞으로 가져오기
시간복잡도 : O(n^2)
공간 복잡도 : O(N)
"""
# for i in range(len(array)):
#     min_idx = i
#     for j in range(i+1, len(array)):
#         if array[min_idx] > array[j]:
#             min_idx = j
#     array[i], array[min_idx] = array[min_idx], array[i]

# print(array) 

"""
삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
시간복잡도 : O(n^2)
최선의 경우 : O(n) ---> 거의 정렬 되어있는 경우 빠르게 동작한다.
공간 복잡도 : O(N)
"""

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j - 1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
# print(array)

"""
퀵정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.
일반적인 상황에서 제일 많이 사용되는 정렬 알고리즘
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘 =
==> 병합 또는 퀵 체택한 하이브리드 방식 = C 자바 파이썬 등
피벗 - 주로 첫번째 데이터
왼쪽에서부터 피벗보다 큰거, 오른쪽에서부터 피벗보다 작은거 골라서 swap
엇갈리면 피벗과 작은값 swap
===> 피벗을 중심으로 왼쪽 작은거, 오른쪽 큰거로 됨.
이 과정 반복 진행

시간 복잡도 : O(NlogN)
최악의 경우 O(N^2) -> 피벗을 잘못 선택(피벗이 안움직일때)
공간 복잡도 : O(N)
"""
# def quick_sort(array, start, end):
#     if start >= end:
#         return
    
#     pivot = start
#     left = start + 1
#     right = end
#     while(left<=right):
#         while(left<=end and array[left]<=array[pivot]):
#             left+=1
#         while(right>start and array[right]>=array[pivot]):
#             right-=1
#         if(left>right):
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]

#     quick_sort(array, start, right -1)
#     quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array)-1)
# print(array)

"""
계수정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 알고리즘
데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
시간복잡도, 공간복잡도 : O(N+K)   - N 데이터 개수 K 데이터 중 최대값
동일한 값을 가진 데이터가 여러개 등장할 때 효과적

인덱스 초기화(데이터 범위만큼)
하나씩 확인하면서 인덱스에 카운트 증가
순서대로 하나씩 그 값만큼 반복하여 인덱스 출력
"""

# count = [0] * (max(array)+1)

# for i in range(len(array)):
#     count[array[i]] += 1
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')

# 파이썬 라이브러리
# array.sort()
# print(array)

# 문제1 : 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# a최소값 b최대값 swap
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

