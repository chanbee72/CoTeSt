import sys

N, M = map(int, sys.stdin.readline().split())

miro = []
for _ in range(N):
    input = sys.stdin.readline()
    line = [int(i) for i in input[:-1]]
    miro.append(line)

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

def miro_print(miro):
    for i in miro:
        print(i)
    print()

def dfs(x, y):
    print(x, y)
    miro_print(visited)

    for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + i[0], y + i[1]

        if 0<=nx<N and 0<=ny<M and miro[nx][ny]:
            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] +1
                if nx == N-1 and ny == M-1:
                    return
                dfs(nx, ny)


dfs(0, 0)