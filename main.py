"""Simple demo app used by the GitHub Actions workflow.

This script provides two commands:
- `hello`: prints a greeting and creates a marker file to signal success.
- `test`: only runs if the `hello` command has previously succeeded (marker file exists).

The workflow can use this to demonstrate conditional execution between jobs.
"""

import argparse
import os
import sys

MARKER_FILE = ".hello_succeeded"


def hello() -> int:
    """Run the hello step and create a marker file on success."""
    print("Hello from myapp!")

    try:
        with open(MARKER_FILE, "w", encoding="utf-8") as f:
            f.write("ok")
    except OSError as exc:
        print(f"Failed to write marker file: {exc}")
        return 1

    return 0


def test() -> int:
    """Run tests only if the hello step succeeded (marker file exists)."""
    if not os.path.exists(MARKER_FILE):
        print("Skipping tests: hello step did not run successfully.")
        return 1

    print("Running tests...")
    # Placeholder for real test commands.
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Demo app for conditional CI jobs.")
    parser.add_argument("command", choices=["hello", "test"], help="Command to run")
    args = parser.parse_args(argv)

    if args.command == "hello":
        return hello()
    return test()


if __name__ == "__main__":
    raise SystemExit(main())
