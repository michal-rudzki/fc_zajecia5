import sys

FILEDB = 'magazyn.db'

def check_warehouse(warehouse, data):
    for product in warehouse:
        if product == data:
            return True
    return False

def open_db_file(file):
    data = []
    print(f"Otiweram do czytania: {file}")
    with open(file, mode = 'r') as f:
        data = f.readlines()
    
    return data

def save_db_file(file):
    pass

def update_warehouse(data_from_file):
    for data in data_from_file:
        print(data)
    
def main():
    data = []
    konto = []
    data_review = []
    
    data_from_file = open_db_file(FILEDB)
    update_warehouse(data_from_file)

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
    
    data_review = data
        
    for arg in sys.argv[1:]:
        data.append(arg)
        
    for loop in range(len(data)):
        if data[0] == 'saldo':
            if not warehouse[data[0]]:
                warehouse.update({len(warehouse[data[0]]):{data[0]:{int(data[1]):data[2]}}})
            warehouse[data[0]].update({len(warehouse[data[0]]):{int(data[1]):data[2]}})
            data = data[3:]
            if len(data) == 0:
                break
        elif data[0] == 'sprzedaż':
            if not warehouse[data[0]]:
                warehouse.update({data[0]:{data[1]:{data[2]:int(data[3])}}})
                warehouse['saldo'].update({len(warehouse['saldo']):{int(data[2]):data[1]}})
            warehouse[data[0]].update({data[1]:{data[2]:int(data[3])}})
            if warehouse['magazyn'][data[1]] - warehouse[data[0]][data[1]][data[2]] >= 0:
                warehouse['magazyn'][data[1]] = warehouse['magazyn'][data[1]] - warehouse[data[0]][data[1]][data[2]]
                warehouse['saldo'].update({len(warehouse['saldo']):{int(data[2]):data[1]}})
            else:
                print("za mało w magazynie")
            data = data[4:]
            if len(data) == 0:
                break
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
                if len(data) == 0:
                    break
            else:
                warehouse[data[0]].update({data[1]:{data[2]:int(data[3])}})
                warehouse['magazyn'].update({data[1]:int(data[3])})
                warehouse['saldo'].update({len(warehouse['saldo']):{(int(data[2])*-1):data[1]}})
                data = data[4:]
                if len(data) == 0:
                    break
        # dodac do magazynu z cli
        elif data[0] == 'magazyn':
            for product in data[1:]:
                if check_warehouse(warehouse['magazyn'], product) != True:
                    warehouse['magazyn'].update({product:0})
                    if len(data[4:]) == 0:
                        data = ['stop']
                        break
                
    if sys.argv[1] == 'magazyn':
        print('M A G A Z Y N')
        for key, value in warehouse['magazyn'].items():
            print(f"{key}: [{value}]")
    elif sys.argv[1] == 'konto':
        for key, value in warehouse['saldo'].items():
            konto += value.keys()
        print(f"Stan konta: {sum(konto)}")
    elif sys.argv[1] == 'przegląd':
        history = {}
        index = 0
        for review in data_review:
            if review == 'saldo':
                history.update({index:data_review[0:3]})
                data_review = data_review[3:]
                #print(history[index])
                index += 1
            elif review == 'zakup' or review == 'sprzedaż':
                history.update(({index:data_review[0:4]}))
                data_review = data_review[4:]
                #print(history[index])
                index += 1
        if int(sys.argv[3])+1 <= index:
            for review in range(int(sys.argv[2]), int(sys.argv[3])+1):
                for format_history in history[review]:
                    print(format_history)
        else:
            print(f"Index poza zasiegiem, index = [{index-1}]")
    elif sys.argv[1] == 'saldo':
        for data in data_review:
            print(data)
    elif sys.argv[1] == 'zakup':
        saldo = []
        zakup = sys.argv[3]
        
        for key, values in warehouse['saldo'].items():
            for saldo_list in values.keys():
                saldo.append(saldo_list)
        
        if sum(saldo) >= int(zakup):
            for data in data_review:
                print(data)
        else:
            print("Za mało środków")
    elif sys.argv[1] == 'sprzedaż':
        for data in data_review:
            print(data)
        
if __name__ == "__main__":
    main()