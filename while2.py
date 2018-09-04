number_str = input("prompt for number: ")
number_int = int(number_str)
sum_of_divisors_str = input("prompt for sum_of_divisors: ")

divisor = 1
sum_of_divisors = 0
while divisor < number_int:
    if number_int % divisor == 0:   # divisor evenly divides theNum
        sum_of_divisors = sum_of_divisors + divisor
    divosor = divisor + 1


