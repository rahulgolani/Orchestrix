import paramiko

class SSHConnection:
    def __init__(self,host,username,password=None,port=2220):
        self.host=host
        self.username=username
        self.password=password
        self.port=port

        self.client=None

    def connect(self):
        self.client=paramiko.SSHClient()

        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            )

    def close(self):
        if self.client:
            self.client.close()
            self.client=None

