"""CLI to the module."""
import argparse

from .{{ cookiecutter.module_name }} import hello_world


def main():
    """Main function for the cli, taking care of the user facing parts."""
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("who", help="Persons to say hello to", default="World", nargs="?")
    args = args_parser.parse_args()

    print(hello_world(args.who))
