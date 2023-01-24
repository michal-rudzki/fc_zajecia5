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
    
    #if sys.argv[1] == 'zakup':
    #    for arg in range(len(sys.argv)-1):
    #        data.append(sys.argv[arg+1])
    #    
    #    for data_count in data:
    #        print(data_count)

if __name__ == "__main__":
    main()