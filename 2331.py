import sys

A, P = map(int, sys.stdin.readline().split())

D = [A]

def make_sequence(a, p):
    num = 0
    for s in str(a):
        num += int(s)**p
    
    if num in D:
        return num
    else:
        D.append(num)
        last_num = make_sequence(num, p)

    return last_num
    

last_num = make_sequence(A,P)
answer = D.index(last_num)
print(answer)