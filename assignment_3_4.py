'''
Write a program using a while statement, that given an int as the input, prints all the factors of that number, 
one in each line.
For example, if the input is
15
The output will be
1
3
5
15
'''

n = int(input("Input an int: ")) # Do not change this line

counter = 1

print(counter)
while counter <= n:
    counter += 1
    if n % counter == 0:
        print(counter)