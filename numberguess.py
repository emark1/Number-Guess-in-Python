import random


print('-----------')
print('GUESS THAT NUMBER SON')
print('-----------')
print()
my_number = random.randint(0, 100)


guess = -1
name = input("What is your name? ")

while guess != my_number:
    text_guess = input('Guess the number please: ')
    guess = int(text_guess)

    if guess < my_number: 
        print("The guess of " + text_guess + " was too low!")
    elif guess > my_number:
        print("Sorry, {0}. That guess of {1} was too high!".format(name, guess))
    else:
        print("YOU GOT IT BUD")

