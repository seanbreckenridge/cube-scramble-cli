#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from os import path, environ
from collections import OrderedDict
import argparse
from typing import Optional, Tuple

from tabulate import tabulate
from prompt_toolkit import PromptSession  # type: ignore[import]
from prompt_toolkit.history import FileHistory # type: ignore[import]
from prompt_toolkit.completion import WordCompleter # type: ignore[import]
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory  # type: ignore[import]
from pyTwistyScrambler import scrambler333, scrambler444, scrambler222, scrambler555, scrambler666, scrambler777, pyraminxScrambler, megaminxScrambler, squareOneScrambler, skewbScrambler, clockScrambler # type: ignore[import]

from cube_scramble_cli.stopwatch import stopwatch

def get_help() -> str:
    return """
{}

Add a number after a symbol to print multiple scrambles. e.g.: 3x3 5
""".format(tabulate(help_lines, headers=["Scramble", "Key"], tablefmt="rst"))


help_lines = [
    ['3x3 WCA Scramble', '3x3'],
    ['2x2 WCA Scramble', '2x2'],
    ['4x4 WCA Scramble', '4x4'],
    ['5x5 WCA Scramble', '5x5'],
    ['6x6 WCA Scramble', '6x6'],
    ['7x7 WCA Scramble', '7x7'],
    ['Pyraminx Scramble', 'PYRAMINX'],
    ['Megaminx Scramble', 'MEGAMINX'],
    ['Square-1 Scramble', 'SQUARE ONE'],
    ['Skewb Scramble', 'SKEWB'],
    ['Clock scramble', 'CLOCK'],
    ['First 2 Layers Scramble', 'F2L'],
    ['<RU>-gen Scramble', 'RU'],
    ['<MU>-Last Six Edges Scramble', 'LSE'],
    ['CMLL Scramble', 'CMLL'],
    ['Corners of the Last Layer Scramble', 'CLL'],
    ['Edges of the Last Layer Scramble', 'ELL'],
    ['Last Layer Scramble', 'LL'],
    ['Last Slot and Last Layer Scramble', 'LSLL'],
    ['[Stopwatch]', 'STOPWATCH'],
    ['[Print Help]', 'HELP'],
    ['[Quit]', 'QUIT']
]

non_prompt_symbols = ["HELP", "QUIT"]
non_scramble_symbols = ["STOPWATCH"] + non_prompt_symbols

scrambles = OrderedDict([
    ('3x3', scrambler333.get_WCA_scramble),
    ('2x2', scrambler222.get_WCA_scramble),
    ('4x4', scrambler444.get_WCA_scramble),
    ('5x5', scrambler555.get_WCA_scramble),
    ('6x6', scrambler666.get_WCA_scramble),
    ('7x7', scrambler777.get_WCA_scramble),
    ('PYRAMINX', pyraminxScrambler.get_WCA_scramble),
    ('MEGAMINX', megaminxScrambler.get_WCA_scramble),
    ('SQUARE ONE', squareOneScrambler.get_WCA_scramble),
    ('SKEWB', skewbScrambler.get_WCA_scramble),
    ('CLOCK', clockScrambler.get_WCA_scramble),
    ('LL', scrambler333.get_LL_scramble),
    ('F2L', scrambler333.get_F2L_scramble),
    ('LSE', scrambler333.get_2genMU_scramble),
    ('CMLL', scrambler333.get_CMLL_scramble),
    ('CLL', scrambler333.get_CLL_scramble),
    ('ELL', scrambler333.get_ELL_scramble),
    ('LSLL', scrambler333.get_LSLL_scramble),
    ('RU', scrambler333.get_2genRU_scramble),
    ('STOPWATCH', stopwatch),
    ('HELP', get_help),
    ('QUIT', sys.exit)
])

history_location = environ.get("SCRAMBLE_HISTORY", path.join(path.expanduser("~"), ".scramble_history.txt"))

symbol_completer = WordCompleter(
    list(scrambles.keys()) + ["HELP"], ignore_case=True)
session = PromptSession(
    history=FileHistory(history_location),
    completer=symbol_completer,
    auto_suggest=AutoSuggestFromHistory())  # type: ignore[var-annotated]


def parse_user_input(string_from_user: str, selected_scramble: Optional[str]) -> Tuple[str, int]:
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


def user_input(selected_scramble: Optional[str]) -> Tuple[str, int]:
    """Asks user for input, converts to corresponding scramble"""
    while True:

        # get input from user
        try:
            prompt_text = "> " if selected_scramble is None or selected_scramble in non_prompt_symbols else f"[{selected_scramble}]> "
            resp: str = session.prompt(message=prompt_text).strip().upper()
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


def main() -> None:
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
    current_scramble: Optional[str] = None
    while True:
        current_scramble, count = user_input(current_scramble)  # type: ignore[misc]
        scramble_func = scrambles[current_scramble]  # type: ignore[index]
        if current_scramble in non_scramble_symbols:  # QUIT, HELP, STOPWATCH
            count = 1
        if count <= 1:
            print(scramble_func())
        else:
            for n in range(count):
                print(f"{n+1}. {scramble_func()}")


if __name__ == "__main__":
    main()
