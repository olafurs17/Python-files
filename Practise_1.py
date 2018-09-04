'''
sum1 = input('Input for sum1: ')
sum2 = input('Input for sum2: ')
sum = int(sum1) + int(sum2)
print('The SUM:       ', (sum))

sum1 = input('Input for sum1: ')
sum2 = input('Input for sum2: ')
sum3 = input('Input for sum3: ')
sum = int(sum1) + int(sum2) + int(sum3)
print('The SUM is :',(sum))

sum1 = input('Input for sum1: ')
sum2 = input('Input for sum2: ')
sum = sum1 + sum2
print('There product: ', (sum))

name_str = input('Name: ')
age_int = input('Age: ')
print('Hello my name is',name_str,'and my age is',age_int,)

firstname = input('What is your Firstname? ')
lastname = input('What is your Lastname? ')
fullname = firstname +' '+ lastname
print('Your fullname is ',fullname)

# Celsius to Fahrenheit
# (degrees in celsius) * 9/5 + 32
celsius_int = int(input('Input the temperatur in celsius: '))
fahrenheit_float = (celsius_int * (9/5)) + 32
fahrenheit_int = int(fahrenheit_float)
print('Celsius scale: ', celsius_int)
print('Fahrenheit scale:', fahrenheit_int)

sum1 = int(input('Punch firstnumber: '))
sum2 = int(input('Punch secondnumber: '))
if sum1 > sum2:
    print('The greater integer is Firstnumber =', sum1)
elif sum2 > sum1:
    print('The greater integer is Secondnumber =', sum2)
else:
    print('The numbers are equal!')

string1 = str(input('Punch firststring: '))
string2 = str(input('Punch secondstring: '))
if len(string1) == len(string2):
    print('The strings are at the same lenght !!!')

sum1 = int(input('Punch firstnumber: '))
sum2 = int(input('Punch secondnumber: '))
sum3 = int(input('Punch thirdnumber: '))
if sum1 < sum2 and sum1 < sum3:
    print('The smallest integer is the firstnumber =', sum1)
elif sum2 < sum1 and sum2 < sum3:
    print('The smallest integer is the secondnumber =', sum2)
elif sum3 < sum1 and sum3 < sum2:
    print('The smallest integer is the thirdnumber =', sum3)

number = int(input('Punch the number: '))
if number >= 0 and number < 10:
    print('Less than 10')
elif number >= 10 and number < 20:
    print('Between 10 and 20')
elif number >= 20:
    print('the value is to high!')
elif number <= -1:
    print('too low')

a = int(input('Punch number for a: '))
b = int(input('Punch number for b: '))
while True:
    choice = int(input('Punch number for choice: '))
    if choice == 1:
        print('Summa a og b =', (a + b))
    elif choice == 2:
        print('b dregið frá =', (b - a))
    elif choice == 3:
        print('margfalda saman a og b =', (a * b))
    else:
        print('Invalid input!!!')
        break
'''
for i in range(-5, 11):
    print(i)


