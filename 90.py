import random

number = random.randint(1, 10)
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} chances left")
    guess = input("Guess the number : ")
    try :
        guess = int(guess)
        if 0 < guess < 11:
            if guess == number:
                print("You won!")
                break
            elif guess > number:
                print("Try smaller than", guess)
            else:
                print("Try bigger than", guess)

            chances -= 1
        else :
            print("The number must be between 1-10 !")
    except ValueError:
        print("Entry must be a integer")
else:
    print("Game over! The number was", number)
