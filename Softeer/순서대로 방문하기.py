# n x n 그래프, 1은 벽
# m은 지나야 하는 위치의 개수 

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
m_point = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    m_point[i][0] -= 1
    m_point[i][1] -= 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

def print_graph(graph):
    for row in graph:
        print(row)
    print()

def DFS(x, y, m_idx):
    global cnt 
    if [x, y] == m_point[m_idx]:
        if m_idx == m-1:
            cnt += 1
            return
        m_idx += 1  
    
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and not visited[nx][ny]:
            DFS(nx, ny, m_idx)

    visited[x][y] = False
    return

visited = [[False for _ in range(n)] for _ in range(n)]
DFS(m_point[0][0], m_point[0][1], 1)
print(cnt)