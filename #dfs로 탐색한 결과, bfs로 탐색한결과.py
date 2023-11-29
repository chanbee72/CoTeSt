#dfs로 탐색한 결과, bfs로 탐색한결과
#방문 정점이 여러개면 정점 번호가 작은 것부터
#출력 : dfs로 수행한 결과 bfs로 수행한결과

#dfs는 재귀로, bfs는 deque로 구현
#1. 모든 관계를 이차원 배열로 생성 후 확인
#2. 연결된 정점만 받아서 탐색


#1
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)


def bfs(V):
    q = deque([V])
    visited1[V] = True
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1, N + 1):
            if not visited1[i] and graph[V][i]:
                q.append(i)
                visited1[i] = True

def dfs(V):
    visited2[V] = True
    print(V, end = " ")
    for i in range(1, N+1):
        if not visited2[i] and graph[V][i]:
            dfs(i)


dfs(V)
print()
bfs(V)


#2
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def bfs(V):
    q = deque([V])
    visited1[V] = True
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in graph[V]:
            if not visited1[i]:
                q.append(i)
                visited1[i] = True

def dfs(V):
    visited2[V] = True
    print(V, end = " ")
    for i in graph[V]:
        if not visited2[i]:
            dfs(i)


dfs(V)
print()
bfs(V)
