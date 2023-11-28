# from random import randint

# def generator(number_of_passwords, length):
#     all_characters = list(range(33, 126))
#     for n in [0, number_of_passwords-1]:
#         passwd = ""
#         for l in [0, length-1]:
#             char_ascii = randint(all_characters)
#             passwd += chr(char_ascii)
#             char_spec_list = [33, 47] + [58, 64] + [91, 96] +[123, 126]
#             char_upcase = [65, 90]
#             if char_ascii in char_spec_list:
#                 S = "True"
#             else:
#                 S = "False"
#             if char_ascii in char_upcase:
#                 U = "True"
#             else:
#                 U = "False"
        
#         print(f"{n} --> {passwd}  (U: {U}, S: {S})")

# number_of_passwords = 5
# length = 15
# generator(number_of_passwords, length)
#############################
# correction

import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        else:
            return False
        
def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation():
            return True
        else: 
            return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits 
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password:str = ''
    
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    
    return new_password

if __name__ == '__main__':
    new_pass: str = generate_password(length = 3, symbols = True, uppercase = True)
    print(new_pass)
    
        
