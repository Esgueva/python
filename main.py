
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


def _print_welcome():
    """ Wellcome to aplication """
    print('*' * 35)
    print('*    Welcome to Esgueva Company   *')
    print('*' * 35)
    print('| What wolud you like to do today? |')
    print('-' * 34)
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[L]ist   clients')


def _get_client_name():
    """ Return client name """
    return input('What is the client name?')


if __name__ == '__main__':
    """ Main App """
    
    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == 'C':
        create_client(_get_client_name())
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        new_client_name = input('What is the updated client name?')
        update_client(client_name,new_client_name)
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')