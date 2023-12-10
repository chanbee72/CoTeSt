"""
성격유형 검사하기
"""

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]
# result = "TCMA"

survey = ["TR", "RT", "TR"]
choices =[7, 1, 3]
# result = "RCJA"

def solution(survey, choices):
    answer = ''
    
    type_dict = {"RT":0, "CF":0, "JM":0, "AN":0}

    # 입력을 통해 성격 점수 계산
    for s, c in zip(survey, choices):
        if s not in type_dict.keys():
            s = ''.join(sorted(s))
            c = 8 - c       # s, c 반대로 돌리기
        c = c - 4           # +- 점수로 변환
        type_dict[s] += c   # 해당하는 성격 유형에 점수 추가

    # 점수에 따라 answer 결정
    for key in type_dict.keys():
        if type_dict[key] > 0:      # 양수면 뒷 문자  
            answer += key[1]
        elif type_dict[key] <= 0:   # 아니면 앞 문자 (음수인 경우, 동점인 경우(앞 문자가 알파벳 앞 순서))
            answer += key[0]

    return answer

solution(survey, choices)