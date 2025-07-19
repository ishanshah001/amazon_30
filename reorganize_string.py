import heapq
def reorganizeString(self, s: str) -> str:
    dict = {}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    heap = [(-val, key) for key, val in dict.items()]
    
    heapq.heapify(heap)

    n = len(s)

    if n%2==0 and -1*heap[0][0]>(len(s)//2):
        return ""
    elif -1*heap[0][0]>(len(s)//2)+1:
        return ""
    
    res = [''] * n
    i = 0
    while heap:
        count, char = heapq.heappop(heap)
        for _ in range(-count):
            if i >= n: 
                i = 1
            res[i] = char
            i += 2

    return ''.join(res)

    
    
    