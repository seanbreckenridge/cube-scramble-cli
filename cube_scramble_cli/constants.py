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
