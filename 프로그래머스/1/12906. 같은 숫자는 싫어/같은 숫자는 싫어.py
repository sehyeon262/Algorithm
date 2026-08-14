def solution(arr):
    res = []
    res.append(arr[0])
    
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        if a == b:
            continue
        else:
            res.append(b)
    return res