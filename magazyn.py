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
        
    for arg in sys.argv[1:]:
        data.append(arg)
        
    
    ##################################
    # zad. 4
    ##################################
    for loop in range(len(data)):
        if data[0] == 'stop':
            break
        elif data[0] == 'saldo':
            if not warehouse[data[0]]:
                warehouse.update({len(warehouse[data[0]]):{data[0]:{int(data[1]):data[2]}}})
            warehouse[data[0]].update({len(warehouse[data[0]]):{int(data[1]):data[2]}})
            data = data[3:]
        elif data[0] == 'sprzedaż':
            if not warehouse[data[0]]:
                warehouse.update({data[0]:{data[1]:{data[2]:int(data[3])}}})
                warehouse['saldo'].update({len(warehouse['saldo']):{int(data[2]):data[1]}})
            warehouse[data[0]].update({data[1]:{data[2]:int(data[3])}})
            warehouse['magazyn'][data[1]] = warehouse['magazyn'][data[1]] - warehouse[data[0]][data[1]][data[2]]
            warehouse['saldo'].update({len(warehouse['saldo']):{int(data[2]):data[1]}})
            data = data[4:]
        elif data[0] == 'zakup':
            if not warehouse[data[0]]:
                warehouse.update({data[0]:{data[1]:{data[2]:int(data[3])}}})
                warehouse['magazyn'].update({data[1]:int(data[3])})
                warehouse['saldo'].update({len(warehouse['saldo']):{(int(data[2])*-1):data[1]}})
                data = data[4:]
                continue
            # jesli jest to updejct ilosci, jesli nie ma to wpisz
            if check_warehouse(warehouse['magazyn'], data[1]) == True:
                warehouse['magazyn'][data[1]] = warehouse['magazyn'][data[1]] + int(data[3])
                warehouse['saldo'].update({len(warehouse['saldo']):{(int(data[2])*-1):data[1]}})
                data = data[4:]
            else:
                warehouse[data[0]].update({data[1]:{data[2]:int(data[3])}})
                warehouse['magazyn'].update({data[1]:int(data[3])})
                warehouse['saldo'].update({len(warehouse['saldo']):{(int(data[2])*-1):data[1]}})
                data = data[4:]
        # dodac do magazynu z cli
        elif data[0] == 'magazyn':
            for product in data[1:]:
                if check_warehouse(warehouse['magazyn'], product) != True:
                    warehouse['magazyn'].update({product:0})
                    if len(data[4:]) == 0:
                        data = ['stop']
                        break
                
    #######################################
    # magazyn do 4
    #######################################
    if sys.argv[1] == 'magazyn':
        print('M A G A Z Y N')
        for key, value in warehouse['magazyn'].items():
            print(f"{key}: [{value}]")
        

if __name__ == "__main__":
    main()