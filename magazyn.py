import sys
from modules_warehouse import general as ci

MENU_LIST = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przegld', 'koniec']

def main():
    ci.company_info()
    while True:
        ci.show_menu(MENU_LIST)
        user_input = input("->")
        if user_input != "koniec" or user_input != "end":
            if user_input == "saldo":
                print("saldo")
            elif user_input == "sprzedaz":
                print("sprzedaz")
            elif user_input == "zakup":
                print("zakup")
            elif user_input == "konto":
                print("konto")
            elif user_input == "lista":
                print("lista")
            elif user_input == "magazyn":
                print("magazyn")
            elif  user_input == "przeglad":
                print("przeglad")
        else:
            break

if __name__ == "__main__":
    main()
