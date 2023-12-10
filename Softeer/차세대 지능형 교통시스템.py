N, T = map(int, input().split())
signal = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = 0
x, y, d = 1, 1, 0

cross = [] # 지나온 교차로

queue = [(x, y, d, t)]  # (x, y, d, t) 큐
while queue:
    x, y, d, t = queue.pop(0)
    # 현재 위치에서 갈 수 있는 방향
    
    # 신호로 갈 수 있는 방향
    now_signal = signal[x][y][t%4]  # x,y 교차로의 현재 신호
    directions = []                 # 현재 신호에 맞춰서 갈 수 있는 방향
    t += 1
    pass

# 현재 위치(교차로)와 방향과 신호가 있을 때 내가 갈 수 있는 위치(교차로) 찾기
def findNext(x, y, d, signal):
    pass


"""
포기 선언.
"""