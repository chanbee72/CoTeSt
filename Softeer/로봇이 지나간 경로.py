import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())

graph = []
for _ in range(H):
    line = [s for s in sys.stdin.readline()[:-1]]
    graph.append(line)
#line = [s for s in sys.stdin.readline()]
#graph.append(line)

def print_graph(graph):
  for row in graph:
    print(row)
  print()

print_graph(graph)

def A(x, y, d, visited, graph):
  if d == '<':
    nx, ny = x, y - 2
    mx, my = x, y - 1
  elif d == '>':
    nx, ny = x, y + 2
    mx, my = x, y + 1
  elif d == 'v':
    nx, ny = x + 2, y
    mx, my = x + 1, y
  elif d == '^':
    nx, ny = x - 2, y
    mx, my = x - 1, y

  if 0 <= nx < H and 0 <= ny < W and not visited[mx][my] and not visited[nx][ny] and graph[mx][my] == '#' and graph[nx][ny] == '#':
    #print(nx, ny, d, 'A')
    visited[mx][my] = True
    visited[nx][ny] = True
    return nx, ny, d, 'A', visited
  else:
    return _, _, _, False, visited

def R(x, y, d, visited, graph):
    if d == '>':
        d = 'v'
    elif d == 'v':
        d = '<'
    elif d == '<':
        d = '^'
    elif d == '^':
        d = '>'

    #print(x, y, d, 'R')
    return x, y, d, 'R', visited

def L(x, y, d, visited, graph):
  if d == '>':
    d = '^'
  elif d == '^':
    d = '<'
  elif d == '<':
    d = 'v'
  elif d == 'v':
    d = '>'

  #print(x, y, d, 'L')
  return x, y, d, 'L', visited

moving = [[0, 1, '>'], [0, -1, '<'], [1, 0, '^'], [-1, 0, 'v']]

def find_start(graph):
  for i in range(H):
    for j in range(W):
      if graph[i][j] == '#':
        shap_num, d = 0, ''
        for delta in moving:
          nx, ny = i + delta[0], j + delta[1]
          if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == '#':
            shap_num += 1
            d = delta[2]
        if shap_num == 1:
          return i, j, d
            
command = [A, R, L]

def eqal(visited, graph):
  #print_graph(visited)
  #print_graph(graph)

  for i in range(H):
    for j in range(W):
      if (graph[i][j] == '#' and visited[i][j] == False) or (graph[i][j] == '.' and visited[i][j] == True):
        return False

  return True

def BFS(x, y, d, graph):
  command_list = []
  queue = [(x, y, d)]
  queue = deque(queue)
  visited = [[False for _ in range(W)] for _ in range(H)]
  visited[x][y] = True

  while queue:
    x, y, d = queue.popleft()
    print(x, y, d)

    #print_graph(visited)

    for c in command:
      now_x, now_y, now_d, cm, visited = c(x, y, d, visited, graph)
      if cm != False:
        queue.append((now_x, now_y, now_d))
        command_list.append(cm)

    if eqal(visited, graph):
        return command_list

  return -1, -1

# main
start = find_start(graph)
N = 0
print(start)

x, y, d = start[0], start[1], start[2]
command_list = BFS(x, y, d, graph)
print(''.join(command_list).replace('ARL', 'A').replace('RL', ''))

"""

5 8 
#######.
........
........
........
........

9 14
.......###....
.........#....
.####....###..
.#.........#..
.#.#####...###
.#.#...#.....#
.###.###.....#
.....#.......#
.....#########

"""