def solution(phone_book):
    answer = True
    phone_book.sort()
    length = len(phone_book)
    
    for i in range(length-1):
        n = phone_book[i]
        cut = len(n)
        
        if n == phone_book[i+1][0:cut]:
            return False          
            
    return answer