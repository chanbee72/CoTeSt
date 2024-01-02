import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adjR[b].append(a)

s, t = map(int, sys.stdin.readline().split())

def DFS(now, adj, visited):
    if visited[now]==1:
        return
    
    visited[now] = 1

    for neighbor in adj[now]:
        DFS(neighbor, adj, visited)

    return

fromS = [False for _ in range(n+1)]
fromS[t] = 1
DFS(s, adj, fromS)

fromT = [False for _ in range(n+1)]
fromT[s] = 1
DFS(t, adj, fromT)

toS = [False for _ in range(n+1)]
DFS(s, adjR, toS)

toT = [False for _ in range(n+1)]
DFS(t, adjR, toT)

cnt = -2
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1

print(cnt)