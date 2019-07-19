#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cube_scramble_cli import *

symbol_completer = WordCompleter(
    list(scrambles.keys()) + ["HELP"], ignore_case=True)
session = PromptSession(
    history=FileHistory(
        path.join(
            path.expanduser("~"),
            ".scramble_history.txt")),
    completer=symbol_completer,
    auto_suggest=AutoSuggestFromHistory())


def print_help():
    print("""
{}

Add a number after a symbol to print multiple scrambles. e.g.: 3x3 5
""".format(tabulate(help_lines, headers=["Scramble", "Key"], tablefmt="rst")))


def parse_user_input(string_from_user, selected_scramble):
    """Parses the scramble from the user

    >>> parse_user_input("3X3 5", None)
    ('3x3', 5)
    >>> parse_user_input("5", "3x3")
    ('3x3', 5)
    >>> parse_user_input("RU SCRAMBLE 3", "MEGAMINX")
    ('RU SCRAMBLE', 3)
    >>> parse_user_input("SQUARE ONE 10", "4x4")
    ('SQUARE ONE', 10)
    >>> parse_user_input("", "3x3")
    ('3x3', 1)
    >>> parse_user_input("5", "4x4")
    ('4x4', 5)
    """
    parts = string_from_user.split()
    #  if user didn't provide a scramble this time
    if len(parts) == 0:
        if selected_scramble is None:
            raise RuntimeError("You haven't selected a scramble!")
        else:  # if they provided one last time
            return selected_scramble, 1
    # scrambles which have lowercase letters
    if parts[0] in ["3X3", "4X4", "5X5", "6X6", "7X7"]:
        parts[0] = parts[0].lower()

    # get number of scrambles
    count = 1
    try:
        count = int(parts[-1])
        parts.pop()  # remove number of scrambles from key
    except ValueError:
        pass

    # if theres a scramble selected and the user entered a number
    if selected_scramble is not None and len(parts) == 0:
        return selected_scramble, count

    return " ".join(parts), count


def user_input(selected_scramble):
    """Asks user for input, converts to corresponding scramble"""
    while True:

        # get input from user
        try:
            prompt_text = "> " if selected_scramble is None else "[{}]> ".format(
                selected_scramble)
            resp = session.prompt(message=prompt_text).strip().upper()
        except (KeyboardInterrupt, EOFError):
            print()  # print a newline
            sys.exit(0)
        if resp == "HELP":
            print_help()
            continue

        # parse user input
        try:
            scramble_key, count = parse_user_input(resp, selected_scramble)
            if scramble_key not in scrambles:
                print("Could not find the symbol '{}'".format(
                    scramble_key), file=sys.stderr)
                print_help()
                continue
            else:
                return scramble_key, count
        except RuntimeError:
            print("You haven't selected a scramble!", file=sys.stderr)
            print_help()


def main():
    current_scramble = None
    while True:
        current_scramble, count = user_input(current_scramble)
        scramble_func = scrambles[current_scramble]
        if count <= 1:
            print(scramble_func())
        else:
            for n in range(count):
                print(f"{n+1}. {scramble_func()}")


if __name__ == "__main__":
    main()
