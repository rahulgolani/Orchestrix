import paramiko
from orchestrix.result import CommandResult

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

    #execute a command on the remote server and return the output, error, and exit code
    # Linux Server gives 3 streams, stdout-> normal output, stderr->error output
    def execute(self,command):
        if not self.client:
            raise RuntimeError("SSH Connection is not established")

        stdin,stdout,stderr=self.client.exec_command(command)

        output=stdout.read().decode()
        error=stderr.read().decode()
        exit_code=stdout.channel.recv_exit_status()

        return CommandResult(
            command=command,
            stdout=output,
            stderr=error,
            exit_code=exit_code,
        )


    def close(self):
        if self.client:
            self.client.close()
            self.client=None

