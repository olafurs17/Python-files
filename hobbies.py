'''
Create a for loop that prompts the user for a hobby 3 times, 
then appends each one to hobbies.
'''
hobbies = []
for i in range(3):
    hob = input("Enter hobby:")
    hobbies.append(hob)
print(hobbies)

