import argparse
from orchestrix.exceptions import  OrchestrixError

from orchestrix.inventory import Inventory
from orchestrix.executor import Executor

def main():
    parser=argparse.ArgumentParser(
        prog='orchestrix',
        description='Infrastructure Orchestration Simplified',
    )

    # -i and --inventory are the flags, one is shorthand version and another is descriptive version
    parser.add_argument(
        "-i",
        "--inventory",
        required=True,
        help="Path to the inventory file",
    )

    parser.add_argument(
        "host",
        help="Target Host",
    )

    parser.add_argument(
        "-m",
        "--module",
        default="command",
        help="Module to execute",
    )

    parser.add_argument(
        "-a",
        "--args",
        required=True,
        help="Arguments passed to the module",
    )

    args=parser.parse_args()

    inventory=Inventory(args.inventory)

    executor=Executor(inventory)

    try:
        result=executor.run(args.host,args.module,args.args)

    except OrchestrixError as error:
        # parser.error(str(error))
        print(f"\n{args.host} | FAILED")
        print(str(error))
        return

    print(f"\n{args.host} | {'SUCCESS' if result.success else 'FAILED'}")

    if result.stdout:
        print(f"Output:\n{result.stdout}")

    if result.stderr:
        print(f"Error:\n{result.stderr}")

if __name__=="__main__":
    main()
