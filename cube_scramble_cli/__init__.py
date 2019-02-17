# -*- coding: utf-8 -*-

import sys
from os import path
from collections import OrderedDict

from colorama import init
from colorama import Fore, Back, Style
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pyTwistyScrambler import scrambler333, scrambler444, scrambler222, \
    scrambler555, scrambler666, scrambler777, pyraminxScrambler, \
    megaminxScrambler, squareOneScrambler, skewbScrambler, clockScrambler

init()