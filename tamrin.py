import math
num = int(input("please enter a number: "))
th = 0.00000000001
if(num < 0):
    print("invalid number")
elif(num == 0):
    print(0)
elif(num < 1):
    print(1)
elif(num > 1):
    n1 = num
    while(abs(n1 * n1 - num) > th):
        n2 = (n1 + (num/n1))/2
        n1 = n2
    print(n1)