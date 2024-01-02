import sys

# N: 초염기서열의 개수, M: 초염기서열의 길이
N, M = map(int, sys.stdin.readline().split())
superbases = [sys.stdin.readline().rstrip() for _ in range(N)]

count = 0

# 첫번째 좋은 염기서열을 기준으로 하나씩 보면서 맞는건 맞는 바구니에 넣고 안 맞는 건 안 맞는 바구니에 넣어서 갯수 count
def check():
    candidate = [superbases[i] for i in range(N)]
    basket = {}

    while candidate:
        base = candidate.pop()
        basket[base] = []
        for s in candidate:
            is_same = True
            for i in range(M):
                if base[i] != '.' and s[i] != '.' and base[i] != s[i]:
                    is_same = False

            if is_same:
                basket[base].append(s)
        
        for s in basket[base]:
            candidate.remove(s)


    #print(basket)     
    print(len(basket))
        
    
check()

# 문제는 이제 같은 걸로 친 애들끼리 다를 수 있다.
# base랑은 같지만 그 안에서 파벌싸움이 생길 수 있다.
# base가 .인데 들어온 애들은 신경 안쓰고 들어왔을 거 아니야
# 그럼 그건 또 따로 처리해줘야한다.