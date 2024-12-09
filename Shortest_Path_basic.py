"""
최단경로 알고리즘 : 가장 짧은 경로를 찾는 알고리즘

[다익스트라 알고리즘]
특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산한다.
- 음의 간선이 없을 때 정상적으로 동작
- 그리디 알고리즘임. 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다.
- 시간 복잡도 : O(v^2)
- 동작과정:
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3번 4번 과정을 반복

[우선순위 큐]
우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 표준 라이브러리 형태로 지원
- Heap 사용하여 구현 -> 시간복잡도 : O(log(N))

[개선된 다익스트라 알고리즘]
- 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 사용
- 시간복잡도 : O(Elog(v))

[플로이드 워셜 알고리즘]
모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
- 2차원 테이블에 최단 거리 정보를 저장
- 다이나믹 프로그래밍 유형에 속함
- 각 단계마다 특정한 노드 K를 거쳐 가는 경우를 확인한다. Dab = min(Dab, Dak + Dkb)
- 시간복잡도 : O(N^3)




"""

## 다익스트라 알고리즘
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[i]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost

# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("inf")
#     else:
#         print(distance[i])



# 최소 힙
# 파이썬은 기본적으로 최소힙 -> 따라서 오름차순 정렬
# import heapq

# def heapsort(Iterable):
#     h = []
#     result = []
#     for value in Iterable:
#         heapq.heappush(h,value)
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result

# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)


# 개선된 다익스트라 알고리즘
# import sys
# import heapq

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while  q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("inf")
#     else:
#         print(distance[i])


# 플로이드 워셜 알고리즘

# inf = int(1e9)

# n = int(input())
# m = int(input())

# graph = [[inf]*(n+1) for _ in range(n+1)]

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph = [a][b] = 0
    
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if graph[a][b] == inf:
#             print("inf")
#         else:
#             print(graph[a][b], end=" ")
#     print()


# 문제1: 전보
# import sys
# import heapq

# input = sys.stdin.readline
# INF = int(1e9)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while  q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# n, m, start = map(int, input().split())

# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))

# dijkstra(start)

# count = 0
# max_distance = 0

# for d in distance:
#     if d!= 1e9:
#         count +=1
#         max_distance = max(max_distance, d)
    
# print(count-1, max_distance)

# 문제2: 미래도시

inf = int(1e9)

n, m = map(int, input().split())

graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
    
for _ in range(m):
    a, b= map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance == inf:
    print("inf")
else:
    print(distance)
