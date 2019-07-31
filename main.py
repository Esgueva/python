import sys

clients = 'Rodrigo, Julia, Mario, '


def create_client(client_name):
    """ Create new client """
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already is in the client\'s list')


def update_client(client_name, new_client_name):
    """ Update client """
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',' , new_client_name + ',')
    else:
        _client_not_found()


def delete_client(client_name):
    """ Delete client name """
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',','')
    else:
        _client_not_found()
    pass


def search_client(client_name):
    """ Search client name in client list """
    global clients
    clients_list = clients.split(',')
    
    for client in clients_list:
        if client != client_name:
            continue
        else:
            print('The client {} is in the client\'s list'.format(client_name)) 
            return True

    print('The client {} not in the client\'s list'.format(client_name))

            
def list_clients():
    """ List client """
    global clients
    print(clients)


def _add_coma(): # _nombre -> indica que es de uso interno
    """ Add separator """
    global clients
    clients += ', '


def _client_not_found():
    """ Return not found message """
    return print('Client is not in clients list')


def _get_client_name():
    """ Return client name """
    
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()

    return client_name


def _get_command():
    """ Ask command """

    command = None
    
    while not command:
        command = input('Please enter the command: ')
    
    return command.upper()


def _print_welcome():
    """ Wellcome to aplication """
    print('')
    print('')
    print('*' * 36)
    print('*    Welcome to Esgueva Company    *')


def _print_options():
    print('*' * 36)
    print('| What wolud you like to do today? |')
    print('-' * 36)
    print('|         [C]reate client          |')
    print('|         [U]pdate client          |')
    print('|         [D]elete client          |')
    print('|         [S]earch client          |')
    print('|         [L]ist   clients         |')
    print('|         [E]xit   program         |')
    print('-' * 36)
    print('')


def setup():
    command = _get_command()
    if command == 'C':
        create_client(_get_client_name())
        list_clients()
    elif command == 'U':
        old_client_name = _get_client_name()
        new_client_name = input('What is the updated client name?')
        update_client(old_client_name,new_client_name)
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'S':
        search_client(_get_client_name())
    elif command == 'E':
        sys.exit()
    else:
        print('Invalid command')

if __name__ == '__main__':
    """ Main App """
    
    _print_welcome()
    _print_options()
    setup()
    