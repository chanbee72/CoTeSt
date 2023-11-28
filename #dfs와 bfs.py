#dfs와 bfs

# DFS는 재귀, BFS는 queue
# 1. 이차원 리스트 -> 인덱스:노드 - 값:노드들과 연결 여부
# 2. 정점만 입력받아서 찾가는 방식
# popleft()가 구현되어 시간복잡도가 낮은 deque 사용

import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

# 1
graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False]*(n+1)
visited2 = [False]*(n+1)

def bfs(v):
    q = deque([v])
    visited1[v] = True
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visited1[i] == False and graph[v][i] == True:
                q.append(i)
                visited1[i] = True

def dfs(v):
    visited2[v] = True
    print(v, end = " ")

    for i in range(1, n+1):
        if visited2[i] == False and graph[v][i] == True:
            dfs(i)


dfs(v)
print()
bfs(v)



#2
import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def bfs(v):
    q = deque([v])
    visited1[v] = True

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph:
            if not visited1[i]:
                q.append(i)
                visited1[i] = True


def dfs(v):
    visited2[v] = True
    print(v, end = " ")
    for i in graph:
        if not visited2[i]:
            dfs(i)


dfs(v)
print()
bfs(v)
        
















