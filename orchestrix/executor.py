from orchestrix.ssh import SSHConnection
from orchestrix.modules.command import CommandModule
from orchestrix.modules.ping import PingModule

class Executor:
    def __init__(self,inventory):
        self.inventory=inventory
        self.modules={
            "command":CommandModule(),
            "ping":PingModule(),
        }

    def run(self,hostname,module_name,arguments):
        host=self.inventory.get_host(hostname)

        if not host:
            raise ValueError(f"Host '{hostname}' not found in inventory")

        module=self.modules.get(module_name)

        if not module:
            raise ValueError(f"Module '{module_name}' not found")

        connection=SSHConnection(
            host=host['host'],
            username=host['user'],
            password=host['password'],
            port=int(host.get('port',2220)),
        )

        try:
            connection.connect()
            result=module.run(connection, arguments)
            return result
        finally:
            connection.close()