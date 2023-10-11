import random

number = random.randint(1,100)
attempts = 0

print("\t\t\twelcome to 'Guess My Number'!")

print("\nI'm thinking of number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

while True :
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < number :
        print("Higher...")
    elif guess > number :
        print("Lower...")
    else :
        print("You guessed it! The number was",number)
        print("And it only took you",attempts,"tries!")
        break

print("\n\nPress the enter the key to quit.")
