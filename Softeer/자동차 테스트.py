import sys
import bisect

input = sys.stdin.readline

n, q = map(int, input().split())
fuel = list(map(int, input().split()))
fuel.sort()
set_fuel = set(fuel)

for _ in range(q):
    m = int(input())
    if m not in set_fuel:
        print(0)
    else:
        idx = bisect.bisect_left(fuel, m)
        print(idx*(n-idx-1))