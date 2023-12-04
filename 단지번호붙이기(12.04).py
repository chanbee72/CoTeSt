#2667번 단지번호붙이기

#graph = 지도 입력받기
#apt = 1인 집 있으면 해당 인덱스 넣어놓기
#visited = 방문확인
#apt[0]부터 확인하면서 bfs로 찾아가기 + 연결되어 있으면 apt에서 빼고 visited를 1로
#apt 다시 돌면 visited를 2로


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0] * N for _ in range(N)]
apt = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            apt.append((i,j))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs():
    count = 0
    global N
    for x, y in apt:
        count += 1
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            visited[x][y] = count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = count
                    apt.remove((nx, ny))
    return count

count = int(bfs())

list = [0] * (count + 1)

num = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            list[visited[i][j]] += 1

list.sort()
print(count)
for i in range(1, len(list)):
    print(list[i])