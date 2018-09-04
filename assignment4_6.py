'''
Write a Python program using for loops that, given an integer n, prints all the perfect numbers from 1 to n.

A perfect number is an integer whose sum of integer divisiors (excluding the number itself) add up to the number.

For example, 6 is a perfect number because the sum of its integer divisors (1+2+3) is equal to 6.

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print(n)
'''
top_num = int(input("Upper number for the range: ")) # Do not change this 
for n in range(2, top_num + 1):
    sum = 0
    for divisor in range(1, n):
        if  (n % divisor == 0):
            sum = sum + divisor
        if sum == n:
            print(n)
            break
