import sys

def check_warehouse(warehouse, data):
    for product in warehouse:
        if product == data:
            return True
    return False

def main():
    data = []
    warehouse = {
        'saldo': {},
        'sprzedaż': {},
        'zakup': {},
        'magazyn': {}
    }

    while True:
        user_input = input().strip()
        if not user_input or user_input == 'stop':
            break
        data.append(user_input)
        
    for arg in range(len(sys.argv)-2):
        data.append(sys.argv[arg+1])
        
    
    ##################################
    # zad. 4
    ##################################
    for loop in range(len(data)):
        if data[0] == 'saldo':
            if not warehouse['saldo']:
                warehouse.update({data[0]:{int(data[1]):data[2]}})
            warehouse[data[0]].update({int(data[1]):data[2]})
            data = data[3:]
        elif data[0] == 'sprzedaż':
            if not warehouse['sprzedaż']:
                warehouse.update({data[0]:{data[1]:{data[2]:data[3]}}})
            warehouse[data[0]].update({data[1]:{data[2]:data[3]}})
            data = data[4:]
        elif data[0] == 'zakup':
            if not warehouse['zakup']:
                warehouse.update({data[0]:{data[1]:{data[2]:data[3]}}})
                warehouse['magazyn'].update({data[1]:int(data[3])})
                data = data[4:]
            # jesli jest to updejct ilosci, jesli nie ma to wpisz
            if check_warehouse(warehouse['magazyn'], data[1]) == True:
                warehouse['magazyn'][data[1]] = warehouse['magazyn'][data[1]] + int(data[3])
                data = data[4:]
            else:
                warehouse[data[0]].update({data[1]:{data[2]:int(data[3])}})
                warehouse['magazyn'].update({data[1]:int(data[3])})
                data = data[4:]
            

    #print(warehouse)
    #######################################
    # magazyn do 4
    #######################################
    if sys.argv[1] == 'magazyn':
        print('M A G A Z Y N')
        for warehouse_list in warehouse['magazyn']:
            print(warehouse_list)
        

if __name__ == "__main__":
    main()