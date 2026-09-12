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

    connection.connect()

    print(f'Connected to {server["host"]} as {server["user"]}')
    print(f'SSH Connection Successful')

    connection.close()

    print(f'Connection Closed')


    # print('All hosts:')
    # for hostname,details in inventory.get_all_hosts().items():
    #     print(f"{hostname}: {details}")

# python3 -m orchestrix.cli
# -m is for module, it is used to tell python to search through its system path
if __name__ == '__main__':
    main()