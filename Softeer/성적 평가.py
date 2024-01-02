import sys

N = int(sys.stdin.readline())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

total_score = [0 for _ in range(N)]
for i in range(3):
    for j in range(N):
        total_score[j] += scores[i][j]

def merge_sort(arr, idx, l, r):
    if r > l:
        m = (r+l)//2
        merge_sort(arr, idx, l, m)
        merge_sort(arr, idx, m+1, r)
        merge(arr, idx, l, m, r)

def merge(arr, idx, l, m, r):
    new_arr = arr.copy()
    new_idx = idx.copy()
    i, j, k = l, m+1, l
    while i <= m and j <= r:
        if arr[i] >= arr[j]:
            new_arr[k] = arr[i]
            new_idx[k] = idx[i]
            i += 1
            k += 1
        else:
            new_arr[k] = arr[j]
            new_idx[k] = idx[j]
            j += 1
            k += 1

    if i > m:
        for p in range(j, r+1):
            new_arr[k] = arr[p]
            new_idx[k] = idx[p]
            k += 1
    else:
        for p in range(i, m+1):
            new_arr[k] = arr[p]
            new_idx[k] = idx[p]
            k += 1

    for p in range(l, r+1):
        arr[p] = new_arr[p]
        idx[p] = new_idx[p]
    
# scores: 정렬된 점수표, idx: scores의 원래 인덱스
def make_rank(scores, idx):
    rank = [0 for _ in range(N)]

    for i in range(N):
        index = idx[i]
        rank[index] = i+1

        if i > 0:
            prev_index = idx[i-1]
            if scores[i] == scores[i-1]:
                rank[index] = rank[prev_index]

    return rank

"""
idx = [i for i in range(N)]
merge_sort(scores[0], idx, 0, N-1)
print('정렬된 점수', scores[0])
print('원래 인덱스', idx)
rank = make_rank(scores[0], idx)
print('순위표', rank)
"""



for c in range(3):
    score = scores[c]
    idx = [i for i in range(N)]

    merge_sort(score, idx, 0, N-1)
    rank = make_rank(score, idx)
    print(*rank, sep=' ')

idx = [i for i in range(N)]
merge_sort(total_score, idx, 0, N-1)
rank = make_rank(total_score, idx)
print(*rank, sep=' ')
