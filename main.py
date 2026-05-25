import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as file:
        file.write(key)


def load_key():
    with open("key.key","rb") as file:
        key = file.read()
    return key


def add(fernet):
    login = input("Введите логин ")
    password = input("Введите пароль ")
    with open("passwords.txt","w") as file:
        file.write(f'{login}|{fernet.encrypt(password.encode()).decode()}\n')


def view(fernet):
    with open("passwords.txt","r") as file:
        for line in file.readlines():
            data = line.rstrip()
            login,password = data.split("|")
            decrypted_password = fernet.decrypt(password.encode()).decode()
            print(f'Логин: {login}|Пароль: {decrypted_password}')


def main():
    if not os.path.exists("key.key"):
        write_key()  
    key = load_key()
    fernet = Fernet(key)
    while True:
        choice = input('Для добавления пароля введите 1, для просмотра уже существующих введите 2. Введите 3 для выхода')
        if choice == '1':
            add(fernet)
        elif choice == '2':
            view(fernet)
        elif choice == '3':
            break
        else:
            print('Я вас не понял') 


if __name__ == '__main__':
    main()
