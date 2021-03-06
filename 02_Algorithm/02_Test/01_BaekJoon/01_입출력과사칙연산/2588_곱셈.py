# URL : https://www.acmicpc.net/problem/2588

num1 = int(input())
num2 = int(input())

num2_lst = [i for i in str(num2)] # seperate the digits of each number

for i in range(2,-1, -1) : # call in reverse to calculate from low digits
    print(num1 * int(num2_lst[i])) # convert characters to numbers for computational operations
print(num1 * num2)
