lines = list()
n = int(input('How many lines do you want to enter? '))
for i in range(n):
    line = input('Next line: ')
    lines.append(line)
    
print('Your lines were:')
for line in lines:
    print(line)
