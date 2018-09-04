secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = ((secs_int // 60) // 60)
minutes_int = secs_int - hours * 3600
minutes = minutes_int // 60
seconds = (secs_int % 60)
print(hours,":",minutes,":",seconds) # do not change this line
