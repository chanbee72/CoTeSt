import sys

R, C = map(int, sys.stdin.readline().split())

zido = []
water_point = []
for i in range(R):
    line = list(s for s in sys.stdin.readline())
    zido.append(line[:-1])

    if 'S' in line:
        j = line.index('S')
        start_point = [i, j]

    if '*' in line:
        j = line.index('*')
        water_point.append([i, j])

    if 'D' in line:
        j = line.index('D')
        end_point = [i, j]


"""
D는 비버굴(도착지), S는 고슴도치의 위치
*은 물, 물과 인접해있는 비어있는 칸은 물이 참 (돌 통과 X)
X는 돌
물이 찰 예정인 칸으로 이동 불가

start_point : 시작점
end_point   : 도착점
water_point : 물의 위치
"""

moving = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 입력 x, y로 이동할 수 있는지 확인 (돌이 있거나 찰 예정이면 안 됨, 지도 내부인지도 확인)
def check_move(x, y):
    if zido[x][y] == 'X':   # 돌이면 이동 못하고
        return False
    
    if zido[x][y] == 'D':   # 도착지면 이동 가능
        return True
    
    for delta in moving:    # 다음 턴에 물이 차는 곳은 이동 불가 (상하좌우 인접한 곳에 물이 있으면 다음 턴에 물이 차는 곳)
        nx, ny = x + delta[0], y + delta[1]
        
        if check_in(nx, ny) and zido[nx][ny] == '*':
            return False
        
    return True             # 그 외의 경우는 이동 가능

# 입력 x, y가 지도 내에 있는 지 확인
def check_in(x, y):
    if x > R-1 or x < 0 or y > C-1 or y < 0:
        return False

    return True

# 물의 위치 이동
def moving_water(waters, visited_water):
    """
    waters          : 현재 물의 가장자리 위치
    visited_water   : 물이 있는지 없는 지 확인
    new_waters      : 퍼진 후에 물의 가장자리 위치
    """
    new_waters = []
    for water in waters:        # 물이 있는 곳마다
        for delta in moving:    # 상하좌우로 움직이면서
            nx, ny = water[0] + delta[0], water[1] + delta[1]
            if check_in(nx, ny) and zido[nx][ny] != 'X' and zido[nx][ny] != 'D' and not visited_water[nx][ny]:
            # 지도 내부인지, 돌이 있는지, 비버 굴(도착점)인지, 이미 물이 퍼진 곳인지 확인
                zido[nx][ny] = '*'
                new_waters.append([nx, ny])     # 새로운 물의 가장자리 업데이트
                visited_water[nx][ny] = True    # 물이 퍼진 곳 체크

    return new_waters   # 새로운 물의 가장자리 위치 반환

# 지도를 보기 편하게 출력 
def print_map(s, zido):
    print(s)
    for line in zido:
        print(line)

# BFS
def bfs(start, waters):
    queue = [(start[0], start[1], 0)]
    prev_time = 0

    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]] = True

    visited_water = [[0 for _ in range(C)] for _ in range(R)]
    for water in waters:
        visited_water[water[0]][water[1]] = True

    while queue:
        #print()
        #print('Queue', queue)
        #print_map('Visited', visited)
        #print_map('Visited Water', visited_water)
    
        x, y, time = queue.pop(0)
        #print('now', x, y, time)
        
        if prev_time != time:
            #print('Moving Water')
            waters = moving_water(waters, visited_water)

        #print_map('Map', zido)

        if [x, y] == end_point:
            return time

        for delta in moving:
            nx, ny = x + delta[0], y + delta[1]
            if check_in(nx, ny) and check_move(nx, ny):
                #print('next point', nx, ny)
                if not visited[nx][ny]:
                    queue.append([nx, ny, time+1])
                    visited[nx][ny] = True

        prev_time = time



    return "KAKTUS"

result = bfs(start_point, water_point)
print(result)
            