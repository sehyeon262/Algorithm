# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
# 그렇지 않으면 true

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:n]:
            answer = False
    return answer