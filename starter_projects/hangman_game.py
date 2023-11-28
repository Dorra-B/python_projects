# from random import choice

# def run_game():
#     word: str = choice(['apple', 'secret' , 'banana'])
#     username: str = input("What is your name ? >> ")
#     print(f"Welcome to Hangman Game {username} !")
    
#     guessed: str = ''
#     tries: int = 3
    
#     while tries > 3:
#         blanks: int = 0
#         print('Word: ', end='')
#         for char in word:
#             if char in guessed:
#                 print(char, end='')
#             else:
#                 print('_', end='')
        
    ######################
    
# name:str = input('What is your name ? >>  ')
# print(f"Welcome to hangman, {name} !\n")
# tries = 5
# while tries > 0:
#     print("Word: ----")
#     guess = input("Enter a letter: ")
#     if guess.lower() not in range('a','z'): 
#         print("This is not a letter")
#         continue
#     else:
#         print("Good Guess")

        #####################
from random import randint
guess_words_list = ['eye', 'guy', 'why', 'dye','shy']
guess_word = guess_words_list[randint(0,(len(guess_words_list)-1))]
word_format= '_'*len(guess_word)
name: str = input("What is your name >> ")   
print(f"Welcome to hangman, {name}  \n Each underscore represents a letter to guess ")
tries = 4
print(f" Cheat : The word to guess is : >>>>>> {guess_word}")
while (tries > 0) and ('_' in word_format): 
    print(f"Word to guess: {word_format} ")
    letter: str = input("Enter a letter: ")
    if letter.lower() not in [chr(i) for i in range(97,122)]:
        print('This is not a letter')
        continue
    elif letter.lower() not in guess_word:
        print('This letter doesn\'t exist in the word to guess !')
        tries -= 1
        continue
    elif letter.lower() in guess_word:
        for k in range(0, len(guess_word)):
            if guess_word[k] == letter.lower():
                word_format = word_format[:k]+letter.lower()+word_format[k+1:]
                continue           
    if '_' not in word_format:
        print(f"Bravo {name} ! \n You guessed the correct word >>>> {guess_word} \n You Guessed it after {tries} Tries")
    elif (tries == 0) and ('_' in word_format):
        print(f"Sorry {name} ! No more tries left \n You Lost \n Game Is Over !")
                







    