import sys

num_row, num_col = 12, 6

graph = [list(sys.stdin.readline()[:-1]) for _ in range(num_row)]

moving = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 입력 좌표와 함께 터지는 뿌요 위치 반환 (visited)
def is_pop(x, y, graph):
    if graph[x][y] == '.':
        return False
    
    visited = [[0 for _ in range(num_col)] for _ in range(num_row)]
    color = graph[x][y]
    
    queue = [[x, y]]
    visited[x][y] = 1

    while queue:
        x, y = queue.pop(0)

        for delta in moving:
            nx, ny = x + delta[0], y + delta[1]
            if 0<=nx<num_row and 0<=ny<num_col and graph[nx][ny] == color and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1

    total = 0
    for row in visited:
        total += sum(row)
        

    if total >= 4:
        return visited
    
    return False

# 뿌요 터지면 아래로 내림
def down():
    for i in range(num_col):
        col = [graph[j][i] for j in range(num_row)]
        col.reverse()
        new_col = []
        for j in range(num_row):
            if col[j] != '.':
                new_col.append(col[j])

        while len(new_col) != num_row:
            new_col.append('.')
        
        new_col.reverse()

        for j in range(num_row):
            graph[j][i] = new_col[j]

# 더이상 터질게 없는 지 확인 
# 터질게 있으면 좌표 반환
def done():
    is_done = True
    for i in range(num_row):
        for j in range(num_col):
            a = is_pop(i, j, graph)
            if a:
                is_done = False
                for i in range(num_row):
                    for j in range(num_col):
                        if a[i][j]:
                            graph[i][j] = '.'

    return is_done

def puyo():
    count = 0

    while not done():
        down()
        count += 1

    return count

print(puyo())