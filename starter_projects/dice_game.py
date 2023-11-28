############ My Try ################

# from random import randint

# while True:
#     try:
#         n_put = input("How many dices you want to roll ? ")
#         if n_put == "exit":
#             print("Thanks for playing ! ")
#             break
#         else:
#             n_put = int(n_put)
#     except ValueError as e:
#         print("The given input is not a number")
#         continue
#     for r in range(0, n_put):
#         res = []
#         roll = randint(1, 6)
#         res.append(roll)
#         print(*res)

############ Correction ################

import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll ? ")
            if user_input.lower() == "exit":
                print("Thanks for playing ! ")
                break
            print(roll_dice(int(user_input)))
            total = sum(roll_dice(int(user_input)))
            print(f"The sum of your dice essays is: {total}")


        except ValueError:
            print("Please Enter a valid number ")    
            
if __name__=='__main__':
    main()