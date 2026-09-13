from dataclasses import dataclass

# A dataclass is a decorator that generates a boilerplate code for classes that are used to store data
# Python automatically injects special dunder methods like __init__, __repr__, __eq__

@dataclass
class CommandResult:
    command: str
    stdout: str
    stderr: str
    exit_code: int

    @property
    def success(self):
        return self.exit_code == 0