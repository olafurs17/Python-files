'''
Write a Python program using a for loop, that given two integers as input, prints the greatest common divisor (gcd) of them.
GCD is the largest integer that divides each of the two integers.
For example, given the numbers 12 and 15, the output will be:
3
'''
m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(1,n+1):
    if m % i == 0 and n % i == 0:
        gcd = i
print(gcd)


'''
a = input('Please input the first integer:')
b = input('Please input the second integer:')
 
for i in range(1,b+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)
'''