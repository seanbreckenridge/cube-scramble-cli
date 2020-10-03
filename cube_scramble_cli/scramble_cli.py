#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cube_scramble_cli import *

history_location = environ.get("SCRAMBLE_HISTORY", path.join(path.expanduser("~"), ".scramble_history.txt"))

symbol_completer = WordCompleter(
    list(scrambles.keys()) + ["HELP"], ignore_case=True)
session = PromptSession(
    history=FileHistory(history_location),
    completer=symbol_completer,
    auto_suggest=AutoSuggestFromHistory())


def parse_user_input(string_from_user, selected_scramble):
    """Parses the scramble from the user

    >>> parse_user_input("3X3 5", None)
    ('3x3', 5)
    >>> parse_user_input("5", "3x3")
    ('3x3', 5)
    >>> parse_user_input("RU 3", "MEGAMINX")
    ('RU', 3)
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
    if parts[0] in ["2X2", "3X3", "4X4", "5X5", "6X6", "7X7"]:
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
            prompt_text = "> " if selected_scramble is None or selected_scramble in non_prompt_symbols else f"[{selected_scramble}]> "
            resp = session.prompt(message=prompt_text).strip().upper()
        except (KeyboardInterrupt, EOFError):
            print()  # print a newline
            sys.exit(0)

        # parse user input
        try:
            scramble_key, count = parse_user_input(resp, selected_scramble)
            if scramble_key not in scrambles:
                print("Could not find the symbol '{}'".format(
                    scramble_key), file=sys.stderr)
                print(get_help())
                continue
            else:
                return scramble_key, count
        except RuntimeError:
            print("You haven't selected a scramble!", file=sys.stderr)
            print(get_help())


def main():
    parser = argparse.ArgumentParser(
        description="A command line based stopwatch and twisty puzzle scramble generator")
    parser.add_argument(
        "-s",
        "--print-symbols",
        action="store_true",
        help="Print a list of the supported symbols")
    parser.add_argument(
        "-H",
        "--hide-stopwatch",
        action="store_true",
        help="When using the stopwatch, don't display the time while solving")
    args, leftover = parser.parse_known_args()
    if args.print_symbols:
        print(get_help())
        sys.exit(0)
    if args.hide_stopwatch:
        scrambles["STOPWATCH"] = lambda: stopwatch(hide_text=True)
    if leftover:
        try:
            scramble_key, count = parse_user_input(" ".join(leftover), None)
            if scramble_key in scrambles:
                scramble_func = scrambles[scramble_key]
                for _ in range(count):
                    print(scramble_func())
                sys.exit(0)
        except Exception as e:
            print("Failed trying to use CLI args as input: ", str(e), file=sys.stderr)
    current_scramble = None
    while True:
        current_scramble, count = user_input(current_scramble)
        scramble_func = scrambles[current_scramble]
        if current_scramble in non_scramble_symbols:  # QUIT, HELP, STOPWATCH
            count = 1
        if count <= 1:
            print(scramble_func())
        else:
            for n in range(count):
                print(f"{n+1}. {scramble_func()}")


if __name__ == "__main__":
    main()
