def company_info():
    name = "Sklep rowerowy 'Dwa Koła' Sp. z o.o."
    email = "sklep@dwa-kola.pl"
    address = "ul. Rowerowa 45, Gdańsk"
    company_info = [name, address, name]

    return company_info

def show_menu(list_options):
    menu = list_options
    for list in list_options:
        print(f"[] {list}")