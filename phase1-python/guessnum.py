import random

print("I am thinking of a number between 1 and 20.")
no_of_guesses = 0
my_guess = random.randint(1,20)
while True:
    user_guess = int(input(("Take a guess.")))
    no_of_guesses = no_of_guesses + 1
    if my_guess == user_guess:
        print("You are correct.")
        break
    elif my_guess > user_guess:
        print("Your guess is Low.")
    else:
        print("Your guess is High.")    
    continue
print("Good job! You got it in", no_of_guesses, " !")