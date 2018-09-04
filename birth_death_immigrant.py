years_str = input("Years: ") # do not change this line
years_int = int(years_str)
population = 307357870
birth_int = 31536000 / 7
death_int = 31536000 / 13
immigrant_int = 31536000 / 35
new_population = years_int * ((birth_int + immigrant_int) - death_int) + population
# Missing lines here

print("New population after", years_int, " years is ", int(new_population)) # do not change this line
