#TEST WHETHER ORCHESTRIX CAN COMMUNICATE WITH THE REMOTE SERVER

class PingModule:
    name="ping"

    def run(self,connection,arguments):
        result=connection.execute("echo pong")

        return result