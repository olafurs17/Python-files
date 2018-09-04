'''
#i í for lúppunni er breyta og range er fjöldi lína + tölur
#5 í range er efsta talan 0 er talan sem telur niður að
#-1 dregur frá 5 næsta 4 3 2 1
for i in range(5,0,-1):
# i = breyta prentar út stöðu á range
# end=' ' bætir næstu línu aftan við
    print(i, end=' ')
print('Blast off!!')
#5 4 3 2 1 Blast off!!!

for i in range(8):
    #print('*'*6
    print('*'*(i+1))
#prints 1 Olafur 2 Olafur
for i in range(1,101,1):
    print(i,'Olafur')
#prints 1---1 2---4 3---9
for i in range(1,21,1):
    num = i*i
    print(i,'---',num)

# prints 8,11,14,17,,,,
for i in range(8,90,3):
    print(i)
# prints 100,98,96,...4,2
for i in range(100,1,-2):
    print(i)

for i in range(10):
    print('A')
    #print(end=' ')
for i in range(5):
    print('B')
for i in range(4):
    print('CD')
print('E')
for i in range(6):
    print('F')
print('G')

number = input('What is your name?: ')
times_int = input('How many times to print it?: ')
#times_int = int(times)
for i in range(time_int):
    print(time_int, name)

#fibonacci
#hvað á runan að vera löng
number = int(input('How many fib numbers?: '))
#breytur fyrir samlagningu þar sem er samlagning
#á tveim lægri tölum = fibonacci tala
numone = 0
numtwo = 1
#ath. num notað síðan í if setningu og range er 
# látið telja frá 0 up í stærð á  runu
for num in range(0, number):
    if(num <= 1):
        # num breytt í next sem er  notað í að reikna
        #saman fib tölurnar
        next = num
    else:
        #lykkja til að leggja saman tvær neðri tölur fyrir fib
        next = numone + numtwo
        numone = numtwo
        numtwo = next
    print(next)

high = int(input('How high: '))
wide = int(inpu4t('How wide: '))

for i in range(high):
    print('*'*wide)

for i in range(1):
    print('*'*20)
    print('*                  *'*1)
    print('*                  *'*1)
    print('*'*20)

for i in range(4):
    print('*'*(4-i))

for i in range(1):
    print('   *'*1)
    print('  ***'*1)
    print(' *****'*1)
    print('*'*7)
    print(' *****'*1)
    print('  ***'*1)
    print('   *'*1)
  
userInput = int(input("Please input side length of diamond: "))

if userInput > 0:              # Prevents the computation of negative numbers
    for i in range(userInput):
        for s in range (userInput - i) :    # s is equivalent to to spaces
            print("O", end="")
        for j in range((i * 2) - 1):
            print("A", end="")
        print()
    for i in range(userInput, 0, -1):
        for s in range (userInput - i) :
# print("T", end="")
            for j in range((i * 2) - 1):
                print("B", end="")
print()

#userInput = int(input("Please input side length of diamond: "))
userInput =  6


if userInput > 0:               # Prevents the computation of negative numbers
    for i in range(userInput):
        for s in range (userInput - i) :    # s is equivalent to to spaces
            print(" ", end=" ")
        for j in range((i * 2) - 1):
            print("*", end=" ")
        print()

for i in range(userInput, 0, -1):
        for s in range (userInput - i) :
            print(" ", end=" ")
        for j in range((i * 2) - 1):
            print("*", end=" ")
        print()

n=6;
for i in range(n):
    for s in range(n - i):
        print (' ', end="")
    #for i in range((i * 2) - 1):
    for j in range((i * 2) - 1):
        print('*', end="")
    print()
--------------------------------------------
for [first iterating variable] in [outer loop]: # Outer loop
    [do something]  # Optional
    for [second iterating variable] in [nested loop]:   # Nested loop
        [do something]  
---------------------------------------------
https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3

for i in range(40):
    for j in range(3,3,1):
        print('*'*(2*j))



for i in range(10):
    print('A', end='')
for i in range(5):
    print('B', end='')
for i in range(4):
    print('CD', end='')
print('E', end='')
for i in range(6):
    print('F', end='')
print('G')

#num_list = [1, 2, 3]
#alpha_list = ['a', 'b', 'c']

for number in range(0, 5):
    print(number, end='')
    for letter in range(5, 9):
        print(letter, end='')
'''
for i in range(1, 11):
    print(i)