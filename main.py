import os
import requests
from time import sleep
from banner import banner

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
    print(banner)

def printer(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(0.22)

def parse(request: dict):
    if type(request['result']) == dict:
        printer('Ваша почта не была слита!')
    elif type(request['result']) == list:
        printer('К сожелению, ваша почта была слита.\nВот подробная информация обо всех сливах:\n')
        text = ''
        for data in request['result']:
            text += '_________\n'
            text += f'Email: {data["line"]}\n'
            text += f'Sources: {data["sources"][0]}\n'
            text += f'Last Breach: {data["last_breach"]}\n'
            text += f'Login&Password: {data["login"]}:{data["pass"]}\n'
            text += '_________\n\n'
        print(text)

def get_data(email):
    try:
        request = requests.get(f'https://2ip.ru/?area=ajaxHaveIBeenPwned&query={email}').json()
    except Exception as error:
        print(f'К сожелению, при обращении к сервису произошла ошибка.\nТекст ошибки:\n{error}')
        return
    parse(request)

def main():
    clear()
    email = input('Введите вашу электронную почту:  ')
    get_data(email)


main()
input('\nPress Enter to close this')
