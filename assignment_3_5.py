'''
A prime number is a whole number greater than 1 whose only factors are 1 and itself.
Write a program using a while statement, that given an int as the input, prints out 
"Prime" if the int is a prime number, otherwise it prints "!Prime".

'''
n = int(input("Input a natural number: ")) # Do not change this line

either = 0
prime = 2

while prime < n:
    if n % prime == 0:
        either = 1
    prime = prime + 1
if either == 0:
    
    if prime:
        print("Prime")
else:
    print("!Prime")

