def fizzBuzz(n):
    lst = []
    for i in range(1, n+1):
        res = ""
        if i%3==0:
            res+="Fizz"
        if i%5==0:
            res+="Buzz"
        if res:
            lst.append(res)
        else:
            lst.append(str(i))
    return lst