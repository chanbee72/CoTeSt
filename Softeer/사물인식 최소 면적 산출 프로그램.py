"""
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

    return height * width

min_area = 100000000000
cal_points = []

def dfs(idx):
    global min_area

    point = points[idx]
    cal_points.append(point)

    prev_color = cal_points[-1][2] if cal_points else 0
    next_color = prev_color + 1

    if next_color > K:
        area = calculate_square(cal_points)
        if min_area > area:
            min_area = area
        
        cal_points.pop()
        return

    if min_area == 0:
        return
    
    for next_idx in range(idx+1, N):
        if points[next_idx][2] == next_color and min_area > calculate_square(cal_points):
            dfs(next_idx)

    cal_points.pop()

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

# solution
def dfs(color, left, right, bottom, top):
    global minArea
    if color == k+1:
        minArea = min(minArea, (right-left)*(top-bottom))
        return
      
    for point in colors[color]:
        x, y = point[0], point[1]
        leftN, rightN = min(left, x), max(right, x)
        bottomN, topN = min(bottom, y), max(top, y)
        if minArea > (rightN-leftN)*(topN-bottomN):  
            dfs(color+1, leftN, rightN, bottomN, topN)

    return

n, k = map(int, input().split())
colors = [[] for _ in range(k+1)]
for _ in range(n):
    point = list(map(int, input().split()))
    colors[point[2]].append(point[:2])

minArea = 2000 * 2000
dfs(1, 1000, -1000, 1000, -1000)
print(minArea)


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