from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    res = a - b
    return list(res.keys())[0]

# res은 key들을 리스트로 바꾼다
# → 그중 첫 번째 key를 꺼낸다
# → 그 이름을 정답으로 반환한다
