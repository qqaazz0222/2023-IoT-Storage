import time
from argparse import ArgumentParser, Namespace
from pathlib import Path


class TargetPath:
    """
    bool(target_path) returns True, if target_path is a mountpoint
    otherwise False is returned
    """

    def __init__(self, path):
        self.path = Path(path)

    def __bool__(self) -> bool:
        """
        This magic method is called if bool(instance) is used.
        """
        return self.path.is_mount()


def get_args() -> Namespace:
    """
    Get the Target Path as str from arguments supplied by command line.
    """
    parser = ArgumentParser()
    parser.add_argument("target", help="Target to observe", type=TargetPath)
    return parser.parse_args()


def tasks() -> None:
    """
    Placeholder to simulate work
    """
    # here must be something to prevent work on
    # same files again and again
    print("Target is a montpoint, doing all tasks")
    for _ in range(20):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print()


def main() -> None:
    # target got it's type from parser.add_argumuent(..., type=TargetPath)
    # target acts like a bool
    # using target with an if-statement will implicit apply bool(target) to get a boolean back
    target = get_args().target
    last_state = None

    while True:
        if target and not last_state:
            last_state = True
            tasks()
        elif not target and last_state:
            print("Target is no longer mounted")
            last_state = False

        # delay until a new check is done
        print("Sleeping 2 seconds")
        time.sleep(2)


if __name__ == "__main__":
    main()
