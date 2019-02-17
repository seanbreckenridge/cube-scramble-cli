#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cube_scramble_cli import *

# White Background + Black Text, Black Background + White Text, Reset
colors = [Back.WHITE + Fore.BLACK, Back.BLACK + Fore.WHITE, Style.RESET_ALL]

help_lines = [
    '3x3 WCA Scramble                           3x3',
    '2x2 WCA Scramble                           2x2',
    '4x4 WCA Scramble                           4x4',
    '5x5 WCA Scramble                           5x5',
    '6x6 WCA Scramble                           6x6',
    '7x7 WCA Scramble                           7x7',
    'Pyraminx Scramble                          PYRAMINX',
    'Megaminx Scramble                          MEGAMINX',
    'Square-1 Scramble                          SQUARE ONE',
    'Skewb Scramble                             SKEWB',
    'Clock scramble                             CLOCK',
    'First 2 Layers Scramble                    F2L',
    '<RU>-gen Scramble                          RU SCRAMBLE',
    '<MU>-Last Six Edges Scramble               LSE',
    'CMLL Scramble                              CMLL',
    'Corners of the Last Layer Scramble         CLL',
    'Edges of the Last Layer Scramble           ELL'
    'Last Layer Scramble                        LL',
    'Last Slot and Last Layer Scramble          LSLL',
    '[Quit]                                     QUIT'
]

# Make all lines the same length
max_line_length = len(max(help_lines, key=len)) + 1
help_lines = [line.ljust(max_line_length) for line in help_lines]

# color help text in alternating colors
# even lines
help_lines[::2] = ["{}{}{}".format(colors[0], line, colors[2]) for line in help_lines[::2]]
# odd lines
help_lines[1::2] = ["{}{}{}".format(colors[1], line, colors[2]) for line in help_lines[1::2]]
help_text = "Use one of the following symbols:\n{}\n\nAdd a number after a symbol to print multiple scrambles. e.g.: 3x3 5\n".format("\n".join(help_lines))


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
    ('RU SCRAMBLE', scrambler333.get_2genRU_scramble),
    ('QUIT', sys.exit)
])

symbol_completer = WordCompleter(list(scrambles.keys()) + ["HELP"], ignore_case=True)
session = PromptSession(history=FileHistory(path.join(path.expanduser("~"), ".scramble_history.txt")),
                        completer=symbol_completer,
                        auto_suggest=AutoSuggestFromHistory())


def get_prompt_text(selected_scramble):
    """Returns the prompt for the corresponding function from available scrambles"""
    if selected_scramble is None:
        return "> "
    for name in scrambles:
        if hash(selected_scramble) == hash(scrambles[name]):
            return f"[{name}]> "


def has_int(s):
    """Returns a bool describing whether or not the string can be converted to an integer"""
    try:
        int(s)
        return True
    except:
        return False


def user_input(selected_scramble):
    """Asks user for input, converts to corresponding scramble"""
    while True:
        try:
            prompt_text = get_prompt_text(selected_scramble)
            resp = session.prompt(message=prompt_text).strip().upper()
            resp_parts = resp.split()  # get first 2 tokens
            if len(resp_parts) == 0:  # input is empty, assume 1 scramble of previously selected scramble
                if selected_scramble is not None:
                    return selected_scramble, 1
                else:
                    raise KeyError  # no input, print help_text
            else:
                if resp_parts[0] in ["3X3", "4X4", "5X5", "6X6", "7X7"]:
                    resp_parts[0] = resp_parts[0].lower()
                elif resp_parts[0] == "HELP":
                    print(help_text)
                    continue
                if len(resp_parts) > 1 and has_int(resp_parts[-1]):  # if the user gave a number denoting multiple scrambles
                    count = int(resp_parts.pop())
                    return scrambles[" ".join(resp_parts)], count
                else:
                    return scrambles[" ".join(resp_parts)], 1  # if no. of scrambles not specified, assume 1 scramble
        except KeyError:
            if not resp.strip():
                print("There was no input!")
            else:
                print("Could not find the symbol '{}'".format(" ".join(resp_parts)))
            print(help_text)
        except (KeyboardInterrupt, EOFError):
            print()  # print a newline
            sys.exit(0)


def main():
    selected_scramble = None
    while True:
        selected_scramble, count = user_input(selected_scramble)
        if count <= 1:
            print(selected_scramble())
        else:
            for n in range(count):
                print(f"{n+1}. {selected_scramble()}")

if __name__ == "__main__":
    main()
