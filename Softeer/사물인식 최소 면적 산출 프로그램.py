import sys

# N: a number of point, K: a number of color, point: [x, y, k(color)]
N, K = map(int, sys.stdin.readline().split())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# points를 색 기준 정렬
points.sort(key=lambda x:x[2])

def calculate_square(points):
    # points: k개의 point
    points_x = [point[0] for point in points]
    points_y = [point[1] for point in points]
    points_x.sort()
    points_y.sort()

    height = points_y[-1] - points_y[0]
    width = points_x[-1] - points_x[0]

    #if (height > min_area and width != 0) or (width > min_area and height != 0): return 1000000

    return height * width

min_area = 1000000
visited = [False for _ in range(N)]
cal_points = []

def dfs(idx):
    global min_area

    point = points[idx]
    cal_points.append(point)
    visited[idx] = True

    prev_color = cal_points[-1][2] if cal_points else 0
    next_color = prev_color + 1

    if next_color > K:
        area = calculate_square(cal_points)
        print(cal_points, area)
        if min_area > area:
            min_area = area
        
        cal_points.pop()
        visited[idx] = False
        return
    
    if min_area == 0:
        return
    
    for next_idx in range(idx+1, N):
        if points[next_idx][2] == next_color and not visited[next_idx]:
            dfs(next_idx)

    cal_points.pop()
    visited[idx] = False

cnt_1 = 1
first_k = points[0][2]
for point in points[1:]:
    if point[2] == first_k:
        cnt_1 += 1
    else:
        break

for i in range(cnt_1):
    dfs(i)
print(min_area)


"""
7 3
-4 0 1
-5 -1 1
0 43 2
3 23 3
8 -19 2
10 0 3
20 0 2

-> 0
"""