import sys
from modules_warehouse import general as ci

MENU_LIST = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przegld', 'koniec']

def main():
    while True:
        ci.show_menu(MENU_LIST)
        user_input = input("->")
        if user_input != "koniec":
            print("menu list")
        else:
            break

if __name__ == "__main__":
    main()
