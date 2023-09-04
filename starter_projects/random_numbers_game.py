from random import randint

lower_num, higher_num= 1, 10
rand= randint(lower_num,higher_num)

print(f" Guess the number in the range between {lower_num} and {higher_num}")
g = 5
while g > 0:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("please enter a valid number: ")    
        continue
    if user_guess > rand:
        g -= 1
        print(" Guessed number is higher than the Correct number ! ")
        print(f"You have {g} guesses left ...")
    elif user_guess < rand:
        g -= 1
        print("Guessed number is lower than the Correct number ! ")
        print(f"You have {g} guesses left ...")
    else:
        print(f"Bravo ! You guessed the Correct number !\n This is your guess number {g}")        
        break
if g==0:
    print("\n\n","*" * 50,"\n\nNo Guesses are left ! ")
    print(f"The correct number is {rand}")        
    