from words import word_list
import random
import os

guessed_letters = []
guessed_words = []
wrong_letters = []
lives = 6


def start(lives):
    word = random.choice(word_list)
    word_as_list = list(word.upper())
    ungessed = ["_" for x in range(len(word_as_list))]
    print(f"\nThe word has {len(word_as_list)} letters.")
    while lives > 0:
        if ungessed == word_as_list:
                print(f"\nCongrats the word was {word.upper()}")
                exit()
        print("\n"+"".join(ungessed))
        guess = input("\nGuess a letter or the word: ").upper()
        if guess in word_as_list:
            print(f"\n{guess} is in the word!\n")
            count = word_as_list.count(guess)
            if  count > 1:
                pindex = -1
                while count > 0:
                    pindex = word_as_list.index(guess,pindex+1)
                    ungessed.pop(pindex)
                    ungessed.insert(pindex,guess)
                    count -= 1
            elif count == 1:
                    index = word_as_list.index(guess)
                    ungessed.pop(index)
                    ungessed.insert(index,guess)

        elif list(guess) == word_as_list:
            print(f"\nCongrats you won! The word was {word.upper()}")
            exit()

        else:
            if guess not in wrong_letters:
                print("\nWrong guess\n")
                lives -= 1
                wrong_letters.append(guess)
                print(mans[lives])
            else:
                print("\nYou have already guessed that word!\n")
        print(f"\nGuessed letters and words: {wrong_letters}")
    if lives == 0:
            print(f"\nYou lost! The word was: {word.upper()}")
            exit()






mans = [
"""
  _________
 |         |
 ○         |
           |
           |
           |
           |
           |
           |
___________|_
""",
"""
  _________
 |         |
 ○         |
 |         |
 |         |
           |
           |
           |
           |
___________|_ 
""", 
"""
  _________
 |         |
 ○         |
\|         |
 |         |
           |
           |
           |
           |
___________|_
""",
"""
  _________
 |         |
 ○         |
\|/        |
 |         |
           |
           |
           |
           |
___________|_
""",
"""
  _________
 |         |
 ○         |
\|/        |
 |         |
/          |
           |
           |
           |
___________|_
""",
"""
 __________
 |         |
 ○         |
\|/        |
 |         |
/ \        |
           |
           |
           |
___________|_
"""
]

mans.reverse()

os.system("cls")
start(lives)