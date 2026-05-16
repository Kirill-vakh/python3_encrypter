from cryptography.fernet import Fernet
from main import load_key
def authorization(login,password,fernet):
    with open('passwords.txt','r') as file:
        for line in file.readlines():
            data = line.rstrip()
            lgn,pwd = data.split('|')
            decrypted_password = fernet.decrypt(pwd.encode()).decode()
            if login == lgn and password == decrypted_password:
                return True
    return False


def main():
    key = load_key()
    fernet = Fernet(key)
    while True:
        login = input('Укажите логин ')
        password = input('Укажите пароль ')
        if authorization(login,password,fernet):
            print('Вы авторизованы')
            break
        else:
            print('Пользователь не найден')


if __name__ == '__main__':
    main()

    