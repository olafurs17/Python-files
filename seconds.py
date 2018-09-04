secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = round((secs_int / 60) / 60, 1)
minutes = round(secs_int / 60, 1)
seconds = round(secs_int / 60)
print(hours,":",minutes,":",seconds) # do not change this line

