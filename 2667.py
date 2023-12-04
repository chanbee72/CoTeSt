import sys

N = int(sys.stdin.readline())

# zido = [[sys.stdin.readline()[:-1]] for _ in range(N)]
zido = []
for _ in range(N):
    input = sys.stdin.readline()[:-1]
    zido.append([int(x) for x in input])

def print_zido(zido):
    for i in zido:
        print(i)
    print()

visited = [[0 for _ in range(N)] for _ in range(N)]

# 단지에 포함되지 않은 집을 찾는 함수
def find_home():
    for i in range(N):
        for j in range(N):
            if zido[i][j] == 1 and not visited[i][j]:
                return i, j
            
    return False

moving = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_neighbor(x, y):
    neighbor = []
    for delta in moving:
        nx, ny = x + delta[0], y + delta[1]

        if nx < N and nx >= 0 and ny < N and ny >= 0:
            if zido[nx][ny] == 1 and not visited[nx][ny] :
                neighbor.append([nx, ny])

    return neighbor

def bfs():
    x, y = find_home()
    i = 1 # 단지 번호
    queue = [[x, y, i]]
    visited[x][y] = i

    while queue or find_home():
        #print_zido(visited)
        if not queue:
            x, y = find_home()
            i += 1
            queue.append([x, y, i])
            visited[x][y] = i

        x, y, i = queue.pop(0)
        neighbor = find_neighbor(x, y)

        for n in neighbor:
            n_x, n_y = n[0], n[1]
            visited[n_x][n_y] = i
            queue.append([n_x, n_y, i])

    return i


num = bfs()
print(num)

result = []
for i in range(1, num+1):
    sum = 0
    for j in range(N):
        sum += visited[j].count(i)
    
    result.append(sum)

result.sort()
for i in result:
    print(i)