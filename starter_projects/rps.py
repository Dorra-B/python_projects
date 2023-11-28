# tries = 3

# while tries > 0:
#     rps: str =  input(print("Welcome to RPS 9000 ! \n rock, paper, or scissors? >> ")) 
#     if rps.strip() not in ['rock', 'paper', 'scissors']:
#         print('This is not a possible choice \nPlease type one of these choices: rock, paper, or scissors ')
#         continue
#     else:
#         print("Thanks for your choice")
#         break

import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')
        self.moves: dict = {'rock':'🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
  
    def play_game(self):
        user_move: str = input('rock, paper, or scissors >>  ').lower().strip()
        
        if user_move == 'exit':
            print('Thanks for playing ! ')
            sys.exit() #exit from program
        
        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()  
        
        computer_move: str = random.choice(self.valid_moves)  
        self.display_moves(user_move, computer_move)
        self.check_move(user_move, computer_move)
        
        
    def display_moves(self, user_move: str, computer_move: str):
        print('---------')
        print(f"You: {self.moves[user_move]} \nComputer: {self.moves[computer_move]}")
        print('--------- \n\n')
        
    def check_move(self, user_move: str, computer_move: str):
        if user_move == computer_move:
            print('It\'s a tie !  \n')
        elif (user_move == 'rock' and computer_move == 'scissors') or (user_move == 'scissors' and computer_move == 'paper') or (user_move == 'paper' and computer_move == 'rock'):
            print('You Won this one ! The Computer lost against YOU !  \n')
        else:
            print('You loose ! The computer won this one ! \n')
            
if __name__== '__main__':
    rps = RPS()
    
    while True:
        rps.play_game()