import sys

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
    
    ##################################
    # zad. 4
    ##################################
    for loop in range(len(data)):
        if data[0] == 'saldo':
            if not warehouse['saldo']:
                warehouse.update({data[0]:{data[1]:data[2]}})
            warehouse[data[0]].update({data[1]:data[2]})
            data = data[3:]
        elif data[0] == 'sprzedaż':
            if not warehouse['sprzedaż']:
                warehouse.update({data[0]:{data[1]:{data[2]:data[3]}}})
            warehouse[data[0]].update({data[1]:{data[2]:data[3]}})
            data = data[4:]
        elif data[0] == 'zakup':
            if not warehouse['zakup']:
                warehouse.update({data[0]:{data[1]:{data[2]:data[3]}}})
            warehouse[data[0]].update({data[1]:{data[2]:data[3]}})
            data = data[4:]
        
    #######################################
    # magazyn do 4
    #######################################
    if sys.argv[1] == 'magazyn':
        print('M A G A Z Y N')
        for arg in range(len(sys.argv)-2):
            data.append(sys.argv[arg+0])

    print(warehouse)
if __name__ == "__main__":
    main()