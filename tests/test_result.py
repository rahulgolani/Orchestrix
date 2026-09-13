
from orchestrix.result import CommandResult

def test_successful_command():
    result=CommandResult(
        command="hostname",
        stdout="server1",
        stderr="",
        exit_code=0,
    )

    assert result.success is True

def test_failed_command():
    result=CommandResult(
        command="bad-command",
        stdout="",
        stderr="command not found",
        exit_code=127,
    )

    assert result.success is False
