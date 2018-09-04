'''
Write a program that generates a random number (0-25) and ask you to guess it. You have five asserts.
Define a random_number with randit between 0-25.
Initialize number_of_guesses to 5.
Use a while loop to let the user keep guessing so long as number_of_guesses is greater than zero.
Ask the user for their guess, just like the example above.
If they guess correctly, print You guessed the number in X tries!.
'''
# random module settur inn
import random
# breytan number búin til og sett inn í breytuna slembi tölur frá 1 til 25 svæði
number = random.randint(1, 25)
# breytan núllstillt
number_of_guesses = 0
# while lykkjan keyrir 5 hringi
while number_of_guesses < 5:
    # sláið in númer milli 1 og 25
    print('Guess a number between 1 and 25:')
    # fallið input tekur við innslegni tölu
    guess = input()
    # breytunni breytt í integer
    guess = int(guess)
    # 1 bætt við number_of_guesses svo lykkjan keyri upp í 5
    number_of_guesses = number_of_guesses + 1
    # ef giskað er á minni tölu en slembi talan þá prentast það út 
    if guess < number:
        print('Your guess is too low')
    # ef giskað er stærri tölu en slembi talan þá prentast það út
    if guess > number:
        print('Your guess is too high')
    # ef giskað er á rétta slembi tölu þá verður break út úr while lykkjunni og forrittið keyrist áfram
    if guess == number:
        break
# ef giskað er á rétta slembi tölu þá prentast út hve oft þú giskaðir
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
# ef giskað er ekki á rétta slembi tölu þá þá prentast út slembi talan 
else:
    print('You did not guess the number. The number was ' + str(number))
       
'''
import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
    '''