import argparse


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

    if args.module!="command":
        parser.error(f"Unsupported module '{args.module}'. Only 'command' module is supported.")

    inventory=Inventory(args.inventory)

    executor=Executor(inventory)

    result=executor.run(args.host, args.args)

    print(f"\n{args.host} | {'SUCCESS' if result.success else 'FAILED'}")

    if result.stdout:
        print(f"Output:\n{result.stdout}")

    if result.stderr:
        print(f"Error:\n{result.stderr}")

if __name__=="__main__":
    main()
