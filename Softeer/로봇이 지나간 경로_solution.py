import sys 

# 제출할때는 다르게 받아야함.
H, W = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()[:-1]) for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directions = ['^', '>', 'v', '<']

def print_graph(graph):
    for row in graph:
        print(row)
    print()

def findDirection(x, y):
    count = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<H and 0<=ny<W and graph[nx][ny] == '#':
            direction = d
            count += 1
        
    return (direction if count == 1 else -1)

def findStart(graph):
    for x in range(H):
        for y in range(W):
            if graph[x][y] == '#':
                direction = findDirection(x, y)
                if direction != -1:
                    return x, y, direction

def Navigate(x, y, d):
    prevD = nowD = d
    graph[x][y] = '.'

    while True:
        #print_graph(graph)
        while prevD == nowD:
            print("A", end='')
            x, y = x + dx[nowD], y + dy[nowD]
            graph[x][y] = '.'
            x, y = x + dx[nowD], y + dy[nowD]
            graph[x][y] = '.'
            
            prevD = nowD
            nowD = findDirection(x, y)

        if nowD == -1:
            return
        elif (nowD - prevD) % 4 == 1:
            print("R", end='')
        elif (nowD - prevD) % 4 == 3:
            print("L", end='')
        
        prevD = nowD

x, y, d = findStart(graph)
print(x+1, y+1)
print(directions[d])

Navigate(x, y ,d)