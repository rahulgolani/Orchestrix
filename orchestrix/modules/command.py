class CommandModule:
    name = "command"

    def run(self,connection,arguments):
        return connection.execute(arguments)