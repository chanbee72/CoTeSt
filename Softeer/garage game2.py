import sys

N = int(sys.stdin.readline())

origin_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N*3)]

def print_graph(graph):
    for line in graph:
        print(line)
    print()

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

# garage에서 (x, y)에 해당하는 칸에 따라 점수 획득하고 그래프 내리기
def BFS(x, y, graph):
    score = 1
    points = {'x':[x], 'y':[y]}

    queue = [(x, y)]
    color = graph[x][y]
    visited = [[False for _ in range(N)] for _ in range(3*N)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 2*N<=nx<3*N and 0<=ny<N and graph[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                points['x'].append(nx)
                points['y'].append(ny)
                score += 1

    # 주변에 같은 색깔 차량이 없어서 터지지도 않고 점수도 없음
    if score == 1:
        return 0, graph

    height = max(points['y']) - min(points['y'])
    width = max(points['x']) - min(points['x'])
    score += height * width

    # 그래프 내리기
    new_graph = [[0 for _ in range(N)] for _ in range(3*N)]

    for col in range(N):
        graph_col = [graph[i][col] for i in range(3*N)]
        for i in range(3*N):
            if visited[i][col] == 0:
                graph_col.append(graph[i][col])
            else:
                graph_col.append(0)
        num_zero = graph_col.count(0)
        new_col = [0 for _ in range(num_zero)]

        for element in graph_col:
            if element != 0:
                new_col.append(element)
        
        for i in range(3*N):
            new_graph[i][col] = new_col[i]

    return score, new_graph

# garage에서 뭉치 내 하나의 xy좌표만을 가지는 리스트 반환
def find_XY(graph):
    visited = [[False for _ in range(N)] for _ in range(3*N)]
    points = []

    for x in range(2*N, 3*N):
        for y in range(N):
            if visited[x][y] :
                continue
            points.append((x, y))
            color = graph[x][y]
            visited[x][y] = True
            queue = [(x, y)]

            while queue:
                x2, y2 = queue.pop(0)

                for i in range(4):
                    nx, ny = x2 + dx[i], y2 + dy[i]
                    if 2*N<=nx<3*N and 0<=ny<N and graph[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    return points

max_score = -1
cnt = 0
total_score = 0
prev_graph = origin_graph

def DFS(x, y):
    global cnt, max_score, total_score

    score, new_graph = BFS(x, y, prev_graph)
    cnt += 1
    total_score += score

    if cnt == 3:
        max_score = max(max_score, total_score)
        total_score = 0
        return
    




    pass

#score, new_graph = BFS(6, 1, origin_graph)
#print(score)
#print_graph(new_graph)

print_graph(origin_graph)
print(find_XY(origin_graph))