from orchestrix.ssh import SSHConnection

class Executor:
    def __init__(self,inventory):
        self.inventory=inventory

    def run(self,hostname,command):
        host=self.inventory.get_host(hostname)

        if not host:
            raise ValueError(f"Host '{hostname}' not found in inventory")

        connection=SSHConnection(
            host=host['host'],
            username=host['user'],
            password=host['password'],
            port=int(host.get('port',2220)),
        )

        try:
            connection.connect()
            result=connection.execute(command)
            return result
        finally:
            connection.close()