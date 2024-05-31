
command = ''
car_status = 'initial'
while True:
    command = input('>').lower()
    if command == 'help':
        print("""
type 'start' - to start the car
'stop' - to stop the car
'quit' - to exit""")
    elif command == 'start' and car_status == 'initial' or command == 'start' and car_status == 'stopped':
        print('Car started, ready to go!')
        car_status = 'started'
    elif command == 'stop' and car_status == 'started':
        print('Car stopped')
        car_status = 'stopped'
    elif command == 'stop' and car_status == 'stopped':
        print('Car was already stopped before')
    elif command == 'stop' and car_status == 'initial':
        print('Car was not started yet, please start the car first')
    elif command == 'start' and car_status == 'started':
        print('Car was already started')
    elif command == 'quit':
        break
    else: 
        print('I don\'t understand that. Please type "help" for the list of commands')