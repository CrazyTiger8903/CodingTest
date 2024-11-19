# 그래프 탐색 알고리즘 : DFS / BFS

"""
# stack
# 파이썬에서는 리스트로 구현 가능
stack = []

stack.append(5)
stack.pop()

print(stack)
print(stack[::-1])
"""
"""
# queue
# 파이썬에서는 라이브러리 사용

from collections import deque

queue = deque()

queue.append(5)
queue.popleft()

print(queue)
queue.reverse()
"""

# 재귀함수 : 자기 자신을 다시 호출하는 함수

# 1번 : 팩토리얼 구현

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))

# 2번 최대공약수 - 유클리드 호제법
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         return(gcd(b, a%b))
    
# print(gcd(192,162))

"""
DFS : 깊이우선탐색
그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘

스택 자료구조 또는 재귀 함수를 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
방문하지 않은 인접 노드가 없으면 스택에서 꺼냄
3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복
"""

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end='')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

"""
BFS : 너비 우선 탐색
그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐 사용

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
3. 2번의 과정을 수행할 수 없을 때까지 반복
"""

# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v=queue.popleft()
#         print(v, end='')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# 음료수 얼려 먹기 문제

# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result+=1

# print(result)


# 미로 탈출

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))