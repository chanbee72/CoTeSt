import sys

N, M = map(int, sys.stdin.readline().split())

miro = []
for _ in range(N):
    input = sys.stdin.readline()
    line = [int(i) for i in input[:-1]]
    miro.append(line)

visited = [[False for _ in range(M)] for _ in range(N)]

def miro_print(miro):
    for i in miro:
        print(i)
    print()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = []
    queue.append([x, y])

    while queue:
        print(queue)
        miro_print(miro)
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if x == N-1 and y == M-1:
                print(miro[N-1][M-1])
                break

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False and miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])

bfs(0, 0)