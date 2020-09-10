from random import randint
import random

hint = ["What would you use to play Doom-2?","The more you have of it, the less you see"]
the_word = ["computer","darkness"]
r=randint(0,1)
the_word=the_word[r]
hint = hint[r]
game_over = False
board = list("*" * len(the_word))
point=0
while not game_over:
    print("")
    print("------------------------------")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    print(f"Point: {point}")
    print(the_word,hint)
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                if board[i]=='*':
                    board[i] = user_guess
                    point = point + randint(1,10)
                else: 
                    print("Word already guessed!")
                    break
        else: 
            print("Incorrect!")
    else:
        if user_guess == the_word:
            print("Correct! Congratulations!")
            game_over = True
        else:
            print("Incorrect, think again.")

# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.