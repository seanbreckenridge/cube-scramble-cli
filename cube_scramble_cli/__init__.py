# -*- coding: utf-8 -*-

import sys
from os import path
from collections import OrderedDict

from tabulate import tabulate
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pyTwistyScrambler import scrambler333, scrambler444, scrambler222, \
    scrambler555, scrambler666, scrambler777, pyraminxScrambler, \
    megaminxScrambler, squareOneScrambler, skewbScrambler, clockScrambler

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
    ['<RU>-gen Scramble', 'RU SCRAMBLE'],
    ['<MU>-Last Six Edges Scramble', 'LSE'],
    ['CMLL Scramble', 'CMLL'],
    ['Corners of the Last Layer Scramble', 'CLL'],
    ['Edges of the Last Layer Scramble', 'ELL'],
    ['Last Layer Scramble', 'LL'],
    ['Last Slot and Last Layer Scramble', 'LSLL'],
    ['[Quit]', 'QUIT']
]

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
