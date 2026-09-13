from orchestrix.modules.ping import PingModule
from orchestrix.modules.command import CommandModule

# We don't want to SSH into the real server just to test whether our ping module calls the connection correctly.
class FakeConnection:
    def execute(self,command):
        assert command=="echo pong"

        return "pong"

def test_ping_module():
    module=PingModule()

    result=module.run(FakeConnection(),"")

    assert result=="pong"

# This is called a mock/fake dependency.


class FakeCommandConnection:
    
    def execute(self,command):
        return f"executed: {command}"

def test_command_module():
    module=CommandModule()
    result=module.run(FakeCommandConnection(),"hostname")

    assert result=="executed: hostname"