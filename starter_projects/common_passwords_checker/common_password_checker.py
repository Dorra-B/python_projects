def check_password(password: str):
    with open('passwords.txt','r') as file:
        common_passwords: list[str] = file.read().splitlines()
        # print(common_passwords)
    
    for i, common_password in enumerate(common_passwords, start=1):
        # print(f'i : {i} and the common_password is : {common_password}')
        if password == '':
            print('This is an empty string ! INVALID CHECK 🚫')
            return
        elif password == common_password:
            print(f'{password} is NOT secure 🚫 , #{i}')
            return      
    print(f'{password} is UNIQUE ✅')

    
        
        
        
def main():
    password: str = input('Enter the password that you want to check: ')
    check_password(password)
    
if __name__ == '__main__':
    main()
