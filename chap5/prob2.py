import random
words = ["difficult", "banana", "apple", "python", "daegu", "catholic","university"]
word = random.choice(words)

jumble_word = list(word)
random.shuffle(jumble_word)
jumble_word = "".join(jumble_word)

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
print("Jumble word:", jumble_word)

guess = input("Your guess: ")

if guess == word:
    print("Correct")
else:
    print("Sorry, that's not correct. The word was:", word)
