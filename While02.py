lines = list()
print('Enter lines of text.')
print('Enter an empty line to quit.')

line = input('Next line: ') # initalise before the loop
while line != '':   # while NOT the termination condition
    lines.append(line)
    line = input('Next line: ') #!! reset value at end of Loop!

print('Your llines were:')
for line in lines:
    print(line)