# While your tea is too hot, add a chip of ice
# if your tea is to hot you would add a litle ice
# until it would be ok.

# range( start , pastEnd , step )
nums = range(1, 11, 1)
print(list(nums))
'''
nums = list()
i = 4
while (i < 9):
    nums.append(i)
    i = i + 2
print(nums)

temperature = 115
while temperature > 112: #first while loop code
    print(temperature)
    temperature = temperature -1

print("The tea is cool enough.")

x = 1
s = 0

while (x < 10):
    s = s + x
    x = x + 1
    if (x == 5):
        break    
else:
    print("The sum of first 10 integers : ",s)
print("The sum of ",x," numbers is :",s)
-------------------------------------------
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
'''