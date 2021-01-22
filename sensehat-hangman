from sense_hat import SenseHat
import time
import random

sense = SenseHat()

word_list = ["hello", "world", "this", "is", "a", "test"]


attempts_left = 5


randomized_word = random.choice(word_list)
word_list = [x for x in randomized_word]
blank_list = ["_" for x in randomized_word]



while True:
    user_input = str("Enter a letter that you think might be in the word: ")
    
    if user_input in randomized_word:
        print("You got a word!")
        for x in blank_list:
            ind = word_list.index(user_input)
            blank_list[ind] = user_input

    elif:
        print("Oops! You guessed wrongly")
        
        attempts_left -= 1
            

    elif attempts_left == 0 or blank_list == word_list:
        print("Game Over!")

