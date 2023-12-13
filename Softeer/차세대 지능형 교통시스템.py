N, T = map(int, input().split())
signal = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# signal_info[i][j][k]: i번째 신호는 j방향에서 들어오고 k방향으로 나가는 신호 (1인 경우)
signal_info = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(13)]
for i in range(4):
    signal_info[i+1][i][(i+1)%4] = 1
    signal_info[i+1][i][(i+2)%4] = 1
    signal_info[i+1][i][(i+3)%4] = 1

    signal_info[i+5][i][(i+2)%4] = 1
    signal_info[i+5][i][(i+3)%4] = 1

    signal_info[i+9][i][(i+1)%4] = 1
    signal_info[i+9][i][(i+2)%4] = 1

junction = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
junction[0][0][1] = 1
junction2 = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1

def update(time, row, col, inDir, outDir, junction, junction2):
    signalNow = signal[row][col][time%4]
    if signal_info[signalNow][inDir][outDir]:
        if outDir == 0 and col != 0:
            junction2[row][col-1][2] = 1
            visited[row][col-1] = 1
        elif outDir == 1 and row != N-1:
            junction2[row+1][col][3] = 1
            visited[row+1][col] = 1
        elif outDir == 2 and col != N-1:
            junction2[row][col+1][0] = 1
            visited[row][col+1] = 1
        elif outDir == 3 and row != 0:
            junction2[row-1][col][1] = 1
            visited[row-1][col] = 1
    return

for time in range(T):
    for row in range(N):
        for col in range(N):
            for inDir in range(4):
                if junction[row][col][inDir]:
                    for outDir in range(4): 
                        update(time , row, col, inDir, outDir, junction, junction2)
                    junction[row][col][inDir] = 1
    junction, junction2 = junction2, junction

count = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 1:
            count += 1
print(count)