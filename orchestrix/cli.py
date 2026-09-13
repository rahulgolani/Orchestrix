from orchestrix.inventory import Inventory
# from orchestrix.ssh import SSHConnection
from orchestrix.executor import Executor

def main():
    inventory=Inventory('inventory.ini')

    executor=Executor(inventory)

    #execute a command on the remote server
    result=executor.run('server1','uname -a')

    # result=executor.run('server1','hostname')

    # result=executor.run('server1','uptime')

    #TEST A FAILURE
    # result=executor.run('server1','command-that-does-not-exist')

    print("\nCommand:", result.command)
    print("Exit Code:", result.exit_code)
    print("Success:", result.success)
    print("Output:", result.stdout)
    print("Error:", result.stderr)

    # print('All hosts:')
    # for hostname,details in inventory.get_all_hosts().items():
    #     print(f"{hostname}: {details}")

# python3 -m orchestrix.cli
# -m is for module, it is used to tell python to search through its system path
if __name__ == '__main__':
    main()