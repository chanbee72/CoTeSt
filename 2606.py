import sys

num_computer = int(sys.stdin.readline())
num_edge = int(sys.stdin.readline())

a = list([] for _ in range(num_computer+1))

for _ in range(num_edge):
    edge = list(map(int, sys.stdin.readline().split()))
    a[edge[0]].append(edge[1])
    a[edge[1]].append(edge[0])

virous = list(False for _ in range(num_computer+1))

def dfs(start):
    print(start)
    virous[start] = True

    for element in a[start]:
        if not virous[element]:
            dfs[element]


queue = [1]

def bfs():
    while queue:
        start = queue.pop(0)
        
        virous[start] = True

        for element in a[start]:
            if not virous[element]:
                queue.append(element)

#bfs()
dfs(1)
print(sum(virous)-1)