# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a,b,a+b))

# sum=0
# for x in range(2,101,2):
#     sum+=x

# print(sum)

import time 
from prime import judgePrime   #判断是否是质数

# day03
# import random

# num = int(random.uniform(1, 100))
# while True:
#     try:
#         guess = int(input("猜猜看这个1~100之间的随机数是："))
#         if guess>num:
#             print("大了！")
#         elif guess<num:
#             print("小了！")
#         else:
#             print("恭喜你猜对了！")
#             break
#     except ValueError:
#         print("请输入数字！")   

# day04
# 1、水仙花数
print('水仙花数:')
for x in range(100,1000):
    a = x//100
    b = x%100//10
    c = x%10
    if a**3+b**3+c**3==x :
        print(x,end=',')

# 2、完美数

print('完美数:')
start = time.clock()
for x in range(2,30):
    if judgePrime(x):
        x1 = 2**x-1
        if judgePrime(x1):
            x2 = 2**(x-1)*x1
            print(x2,end=',')

end = time.clock()
print("\n执行时间:", (end - start), "秒")


