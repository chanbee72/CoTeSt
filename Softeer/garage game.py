import sys

N = int(sys.stdin.readline())

origin_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N*3)]

def print_graph(graph):
    for line in graph:
        print(line)
    print()

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

# 터뜨릴게 있는지 확인
# return: 터뜨릴 수 있는 색깔
def find_pop(sqare):
    x, y = -1, -1

    # 색깔에 맞는 차량의 위치 찾기
    for i in range(N):
        for j in range(N):
            if square[i][j] != 0:
                x, y = i, j
                break
        if x != -1:
            break
    
    # 해당 색깔의 차량이 없으면 score(0) 반환
    if x == -1:
        return score
    pass

# 그래프 내리기
def down_graph(graph, visited):
    visited = [[False for _ in range(N)] for _ in range(2*N)] + visited

    # step1: visited가 True인 놈들 0으로 바꾸기
    for j in range(N):
        for i in range(2*N, 3*N):
            if visited[i][j]:
                graph[i][j] = 0
                visited[i][j] = False
    
    print_graph(graph)

    # step2: 내리기
    for j in range(N):
        col = [graph[i][j] for i in range(3*N)]
        col.reverse()
        new_col = []
        while len(new_col) != 3*N:
            element = col.pop()
            if element == 0:
                new_col.insert(0, element)
            else:
                new_col.append(element)
        

        for i in range(3*N):
            graph[i][j] = new_col[i]
            
    return graph

# square 안에서 bfs로 color에 해당하는 점수와 터질 좌표(visited), 안터지면 False 반환
def bfs(square, x, y):
    color = square[x][y]
    queue = [(x, y)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    pop_point = [(x, y)]

    score = 1

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and square[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                pop_point.append((nx, ny))
                score += 1

    if score == 1:
        return False, False
    
    pop_x = [point[0] for point in pop_point]
    pop_y = [point[1] for point in pop_point]

    height = max(pop_x) - min(pop_x) + 1
    width = max(pop_y) - min(pop_y) + 1

    score += height*width

    return score, visited

# 네모상자가 들어왔을 때 점수를 계산
# return: score
def claculate_score(square):
    score = 0
    i, j, cnt = 0, 0, 0

    while i < N:
        while j < N and cnt != 3:
            score, visited = bfs(square, i, j)
            if score != False:
                down_graph(graph, visited)
                cnt += 1
                j = -1
            j += 1
        i += 1

    return score

def dfs(graph):
    square = graph[-N:]

    for color in find_pop(square):
        pass

graph = origin_graph.copy()
visited = [[False for _ in range(N)] for _ in range(3*N)]

total_score = 0
for _ in range(3):
    print_graph(graph)
    square = graph[-N:]
    score = claculate_score(square)
    total_score += score

print(total_score)