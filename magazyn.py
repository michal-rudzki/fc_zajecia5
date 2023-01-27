import sys

def main():
    data = []
    while True:
        user_input = input()
        if not user_input or user_input == 'stop':
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