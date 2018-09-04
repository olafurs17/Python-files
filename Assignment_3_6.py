'''
Write a program using a while statement, that prints out the two-digit number such that when you square it, 
the resulting three-digit number has its rightmost two digits the same as the original two-digit number.  
That is, for a number in the form AB:
AB * AB = CAB, for some C. 
'''
n = eval(input("Enter number: "))

a = 1

while a < n:            
    print(a * a)
    a += 1