import sys
from api import get_data, get_events

def main():
    if(len(sys.argv) < 2): # if (blank input):
        print("Please input a valid github username as a line argument")
        sys.exit(1) 
        
    username = sys.argv[1]
    response = get_data(username)
        
    if response.status_code == 200:
        print(f'{username} lastest github activity:\n ')
        get_events(response)
            
    else:
        print(f'Unable to fetch data for {username}')
        sys.exit(1)


if __name__ == '__main__':
    main()