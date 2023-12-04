#11559번 Puyo Puyo

#graph = 뿌요
#네 개 이상 붙어있는거 찾아서 count 1 올리기
#graph에서 없어진 애들 찾아서 다시 배열
#다시 붙어있는거 찾기
#반복, 없으면 count 반납

import sys
from collections import deque

input = sys.stdin.readline
graph = []
visited = [[False] * 6 for _ in range(12)]
puyo = 0


for _ in range(12):
    graph.append(list(map(str, input().rstrip())))

list = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def find():
    while 
        for i in range(12):
            for j in range(6):
                if graph[i][j] == '.':
                    continue
                else:
                    result = bfs(graph[i][j], i, j)
                    visited = [[False] * 6 for _ in range(12)]
                if result == 1:
                    find()



def bfs(P, x, y):
    global puyo
    q1 = deque([(x, y)])
    q2 = deque([(x, y)])
    count = 1
    visited[x][y] = count
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] != False and graph[nx][ny] == P:
                q1.append((nx, ny))
                q2.append((nx, ny))
                visited[nx][ny] = count
                count += 1
    if count >= 4:
        puyo += 1
        while q2:
            x, y = q2.popleft()
            for nx in range(x, 0, -1):
                print(nx)
                if graph[nx-1][y] == P:
                    graph[nx][y] = '.'
                else:
                    graph[nx][y] = graph[nx-1][y]
                if nx == 0:
                    graph[nx][y] = 0
        return 1
    else :
        q2.popleft()
        return 0
    
find()