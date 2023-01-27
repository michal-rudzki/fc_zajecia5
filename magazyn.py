import sys

def main():
<<<<<<< HEAD
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
=======
    data = []
    while True:
        user_input = input()
        if not user_input or user_input == 'stop':
>>>>>>> 5b771036ff295ee3d221dc05e631c0e0a9a31f3c
            break
        data.append(user_input)

    for arg in range(len(sys.argv)-1):
        data.append(sys.argv[arg+1])
    for data_count in data:
        print(data_count)
    
    # warehouse products
    warehouse = {}
    
        
    #for count in range(len(data)):
    #    if data[count] == 'zakup':
    #        warehouse.update({data[count+1]:int(data[count+3])})
    #    elif data[count] == 'sprzedaż':
    #        if data[count+1] in warehouse.keys():
    #            #warehouse[data[count+1]] = warehouse[data[count+1]] - data[count+3]
    #            warehouse[data[count+1]] = warehouse[data[count+1]] - int(data[count+3])
            
    
    print(warehouse)
    
if __name__ == "__main__":
    main()