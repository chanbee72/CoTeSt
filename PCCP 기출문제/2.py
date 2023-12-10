from collections import deque

def print_graph(graph):
    for row in graph:
        print(row)
    print()

def solution(land):
    n, m = len(land), len(land[0])

    visited, num = BFS(n, m, land)    # graph = visited

    graph = count_oil(n, m, visited, num)     # graph 오일 뭉치 크기로 업데이트
    #print_graph(visited)
    #print_graph(graph)

    result = 0

    for col in range(m):    # 모든 열에 대해서
        col_oil = {}

        for row in range(n):    # 해당 열의 모든 행에 접근
            visited_num = visited[row][col]
            if visited_num not in col_oil.keys():
                col_oil[visited_num] = graph[row][col]
        
        col_sum = 0
        for key in col_oil.keys():
            col_sum += col_oil[key]

        if result < col_sum:
            result = col_sum

    return result


def BFS(n, m, land):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    moving = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    cnt = 1
    x, y = find_oil(n, m, land, visited)
    visited[x][y] = 1
    queue = deque([[x, y, cnt]])

    while queue:
        x, y, cnt = queue.popleft()

        for delta in moving:
            nx = x + delta[0]
            ny = y + delta[1]

            if 0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = cnt
                queue.append([nx, ny, cnt])

        if not queue: # 연결된 것 못찾았으면
            p, q = find_oil(n, m, land, visited) # 다른 오일 뭉치를 찾음
            if p != -1: # 다른 오일 뭉치 찾았으면 큐에 추가
                cnt += 1
                queue.append([p, q, cnt])
                visited[p][q] = cnt

    return visited, cnt


def find_oil(n, m, land, visited):
    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                return i, j
            
    return -1, -1

def count_oil(n, m, graph, num):
    new_graph = [[0 for _ in range(m)] for _ in range(n)]

    sum_result = []
    for i in range(1, num+1):
        sum = 0
        for row in graph:
            sum += row.count(i)
        sum_result.append(sum)

    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(1, num+1):
        for row in range(n):
            for col in range(m):
                if graph[row][col] == i and not visited[row][col]:
                    new_graph[row][col] = sum_result[i-1]
                    visited[row][col] = 1
    
    return new_graph

land = [[0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0], 
        [1, 1, 0, 0, 0, 1, 1, 0], 
        [1, 1, 1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0, 1, 1]]

land = [[1, 0, 1, 0, 1, 1], 
        [1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 0, 0], 
        [1, 0, 0, 1, 0, 1], 
        [1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 1]]

print(solution(land))