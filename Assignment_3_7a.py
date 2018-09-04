'''
Par of hole 1: 5
Score on hole 1: 6
bogey
Par of hole 2: 4
Score on hole 2: 4
par
Par of hole 3: 3
Score on hole 3: 5
double bogey
Par of hole 4: 4
Score on hole 4: 3
birdie
'''
total = 0
counter = 0

while True:
    entry = int(input("Enter Test score: "))
    if entry == 0: break
    total += entry   # this should be in while loop
    counter += 1

total = total * 1.0
if counter == 0: exit(1)
avg = total / counter
print("Average is: %3.f" % avg + '%')