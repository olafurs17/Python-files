#if tékkar á hvort númer er mínus tala, ef svo er þá breytir tölunni í 0
#ef talan er ekki mínus tala þá prentast ekkert út
'''my_int_str = input("Sláðu inn tölu mínus eða plús: ")
my_int = int(my_int_str)
if my_int < 0:
    my_int = 0
    print(my_int, "Mínus tala núlluð út")
else:
    print("Plús tala")
'''
#if-else tékka á talan er stærri
first_int_str = input("Type in the first number: ")
first_int = int(first_int_str)
second_int_str = input("Type in the second number: ")
second_int = int(second_int_str)
if first_int > second_int:
    print("The first int is bigger!")
else:
    print("The second int is bigger!")
