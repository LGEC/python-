# 判断是否是质数
def judgePrime(item):
    isPrime = True
    for x in range(2,item):
        if item%x==0 :
            isPrime = False

    if isPrime or item==2:
        return True
    else:
        return False 