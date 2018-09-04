'''
Accept d1 and d2, the number on two dices as input.
First, check to see that they are in the proper range for dice (1-6).
If not, print the message "Invalid input". Otherwise, determine the sum.
If the sum is 7 or 11, print "Winner". If the sum is 2, 3 or 12, print "Loser".
Otherwise print the sum.
'''
d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below

if  (d1 not in range(1, 7)) or (d2 not in range(1, 7)):
    print("Invalid input")
else: 
    print("Invalid input")

sum = (d1 + d2)

if sum == 7:
    print("Winner", sum)
elif sum == 12:
    print("Winner", sum)
elif sum == 1:
    print("Loser", sum)
elif sum == 2:
    print("Loser", sum)
elif sum == 3:
    print("Loser", sum)
elif sum == 11:
    print("Loser", sum)
else:
    print("Sum:",sum)
   


