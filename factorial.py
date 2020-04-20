def fact(n, mem):
    if n==1 or n==0:
        return 1
    if n in mem.keys():
        return mem[n]
    mul = n*fact(n-1, mem)
    mem[n] = mul
    return mul


if __name__=='__main__':
    t = 1
    i = 0
    mem = dict()
    while i<t:
        sum = 0
        n = 6
        res = fact(n, mem)
        for j in str(res):
            sum += int(j)  
        print(sum)
        i += 1
