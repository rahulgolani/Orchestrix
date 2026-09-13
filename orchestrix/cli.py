from orchestrix.inventory import Inventory
from orchestrix.ssh import SSHConnection

def main():
    inventory=Inventory('inventory.ini')

    server=inventory.get_host('server1')

    connection=SSHConnection(
        host=server['host'],
        username=server['user'],
        password=server['password'],
    )

    print(f'Connecting to {server["host"]}...')

    #Establish a connection to the remote server
    connection.connect()

    print(f'Connected to {server["host"]} as {server["user"]}')
    print(f'SSH Connection Successful')

    #execute a command on the remote server
    result=connection.execute('uname -a')

    #TEST A FAILURE
    # result=connection.execute('command-that-does-not-exist')

    print("\nCommand:", result['command'])
    print("Exit Code:", result['exit_code'])
    print("Success:", result['success'])
    print("Output:", result['stdout'])
    print("Error:", result['stderr'])

    connection.close()

    print(f'Connection Closed')


    # print('All hosts:')
    # for hostname,details in inventory.get_all_hosts().items():
    #     print(f"{hostname}: {details}")

# python3 -m orchestrix.cli
# -m is for module, it is used to tell python to search through its system path
if __name__ == '__main__':
    main()