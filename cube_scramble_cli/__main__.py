import sys
from os import path, environ
from collections import OrderedDict
from typing import Optional, Tuple, Sequence, Callable, Any, Dict

import click
from tabulate import tabulate
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pyTwistyScrambler import (  # type: ignore[import]
    scrambler333,
    scrambler444,
    scrambler222,
    scrambler555,
    scrambler666,
    scrambler777,
    pyraminxScrambler,
    megaminxScrambler,
    squareOneScrambler,
    skewbScrambler,
    clockScrambler,
)

from .stopwatch import stopwatch


def _help() -> str:
    return f"""
{tabulate(help_lines, headers=["Scramble", "Key"], tablefmt="rst")}

Add a number after a symbol to print multiple scrambles. e.g.: 3x3 5
"""


help_lines = [
    ["3x3 WCA Scramble", "3x3"],
    ["2x2 WCA Scramble", "2x2"],
    ["4x4 WCA Scramble", "4x4"],
    ["5x5 WCA Scramble", "5x5"],
    ["6x6 WCA Scramble", "6x6"],
    ["7x7 WCA Scramble", "7x7"],
    ["Pyraminx Scramble", "PYRAMINX"],
    ["Megaminx Scramble", "MEGAMINX"],
    ["Square-1 Scramble", "SQUARE ONE"],
    ["Skewb Scramble", "SKEWB"],
    ["Clock scramble", "CLOCK"],
    ["First 2 Layers Scramble", "F2L"],
    ["<RU>-gen Scramble", "RU"],
    ["<MU>-Last Six Edges Scramble", "LSE"],
    ["CMLL Scramble", "CMLL"],
    ["Corners of the Last Layer Scramble", "CLL"],
    ["Edges of the Last Layer Scramble", "ELL"],
    ["Last Layer Scramble", "LL"],
    ["Last Slot and Last Layer Scramble", "LSLL"],
    ["[Stopwatch]", "STOPWATCH"],
    ["[Print Help]", "HELP"],
    ["[Quit]", "QUIT"],
]

non_prompt_symbols = ["HELP", "QUIT"]
non_scramble_symbols = ["STOPWATCH"] + non_prompt_symbols

scrambles: Dict[str, Callable[[], Any]] = OrderedDict(
    [
        ("3x3", scrambler333.get_WCA_scramble),
        ("2x2", scrambler222.get_WCA_scramble),
        ("4x4", scrambler444.get_WCA_scramble),
        ("5x5", scrambler555.get_WCA_scramble),
        ("6x6", scrambler666.get_WCA_scramble),
        ("7x7", scrambler777.get_WCA_scramble),
        ("PYRAMINX", pyraminxScrambler.get_WCA_scramble),
        ("MEGAMINX", megaminxScrambler.get_WCA_scramble),
        ("SQUARE ONE", squareOneScrambler.get_WCA_scramble),
        ("SKEWB", skewbScrambler.get_WCA_scramble),
        ("CLOCK", clockScrambler.get_WCA_scramble),
        ("LL", scrambler333.get_LL_scramble),
        ("F2L", scrambler333.get_F2L_scramble),
        ("LSE", scrambler333.get_2genMU_scramble),
        ("CMLL", scrambler333.get_CMLL_scramble),
        ("CLL", scrambler333.get_CLL_scramble),
        ("ELL", scrambler333.get_ELL_scramble),
        ("LSLL", scrambler333.get_LSLL_scramble),
        ("RU", scrambler333.get_2genRU_scramble),
        ("STOPWATCH", stopwatch),
        ("HELP", _help),
        ("QUIT", sys.exit),
    ]
)

repl_history_location = environ.get(
    "SCRAMBLE_HISTORY", path.join("~/.scramble_history.txt")
)

symbol_completer = WordCompleter(list(scrambles.keys()) + ["HELP"], ignore_case=True)
session: PromptSession[str] = PromptSession(
    history=FileHistory(repl_history_location),
    completer=symbol_completer,
    auto_suggest=AutoSuggestFromHistory(),
)


def parse_user_input(
    string_from_user: str, selected_scramble: Optional[str]
) -> Tuple[str, int]:
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
    # if there's a scramble selected and the user entered a number
    if selected_scramble is not None and len(parts) == 0:
        return selected_scramble, count
    return " ".join(parts), count


def user_input(selected_scramble: Optional[str]) -> Tuple[str, int]:
    """Asks user for input, converts to corresponding scramble"""
    while True:
        # get input from user
        try:
            prompt_text = (
                "> "
                if selected_scramble is None or selected_scramble in non_prompt_symbols
                else f"[{selected_scramble}]> "
            )
            resp: str = session.prompt(message=prompt_text).strip().upper()
        except (KeyboardInterrupt, EOFError):
            click.echo()  # print newline
            sys.exit(0)

        # parse user input
        try:
            scramble_key, count = parse_user_input(resp, selected_scramble)
            if scramble_key not in scrambles:
                click.echo(f"Could not find the symbol '{scramble_key}'", err=True)
                click.echo(_help())
                continue
            else:
                return scramble_key, count
        except RuntimeError:
            click.echo("You haven't selected a scramble!", err=True)
            click.echo(_help())


@click.command()
@click.option(
    "-s",
    "--print-symbols",
    default=False,
    is_flag=True,
    help="Print a list of supported scrambles",
)
@click.option(
    "-H",
    "--hide-stopwatch",
    default=False,
    is_flag=True,
    help="When using stopwatch, don't display time while solving",
)
@click.argument("ARGS", nargs=-1, type=click.UNPROCESSED)
def main(print_symbols: bool, hide_stopwatch: bool, args: Sequence[str]) -> None:
    """A command line based stopwatch and twisty puzzle scramble generator"""
    if print_symbols:
        click.echo(_help())
        sys.exit(0)
    if hide_stopwatch:
        scrambles["STOPWATCH"] = lambda: stopwatch(hide_text=True)
    if args:
        try:
            scramble_key, count = parse_user_input(" ".join(map(str.upper, args)), None)
            if scramble_key in scrambles:
                scramble_func = scrambles[scramble_key]
                for _ in range(count):
                    click.echo(scramble_func())
                sys.exit(0)
        except Exception as e:
            click.echo(f"Failed trying to use CLI args as input: {str(e)}", err=True)
    current_scramble: Optional[str] = None
    while True:
        current_scramble, count = user_input(current_scramble)  # type: ignore[misc]
        scramble_func = scrambles[current_scramble]
        if current_scramble in non_scramble_symbols:  # QUIT, HELP, STOPWATCH
            count = 1
        if count <= 1:
            click.echo(scramble_func())
        else:
            for n in range(count):
                click.echo(f"{n+1}. {scramble_func()}")


if __name__ == "__main__":
    main()
