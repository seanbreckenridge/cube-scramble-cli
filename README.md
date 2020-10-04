# cube-scramble-cli

[![PyPi version](https://img.shields.io/pypi/v/cube_scramble_cli.svg)](https://pypi.python.org/pypi/cube_scramble_cli) [![Python 3.6|3.7](https://img.shields.io/pypi/pyversions/cube_scramble_cli.svg)](https://pypi.python.org/pypi/cube_scramble_cli) [![Build Status](https://travis-ci.com/seanbreckenridge/cube-scramble-cli.svg?branch=master)](https://travis-ci.com/seanbreckenridge/cube-scramble-cli) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

A CLI for [pyTwistyScrambler](https://github.com/euphwes/pyTwistyScrambler), to generate random states for Rubik's cubes/twisty puzzles.

<img src="https://raw.githubusercontent.com/seanbreckenridge/cube-scramble-cli/master/.github/demo.gif" alt="cube-scramble-cli demo gif">

#### Installation

Requires python3.6+

`$ pip3 install cube-scramble-cli`

#### Run

`$ cube-scramble-cli`

```
❯ cube-scramble-cli -h
usage: cube-scramble-cli [-h] [-s] [-H]

A command line based stopwatch and twisty puzzle scramble generator

optional arguments:
  -h, --help            show this help message and exit
  -s, --print-symbols   Print a list of the supported symbols
  -H, --hide-stopwatch  When using the stopwatch, don't display the time while
                        solving
```

Supported Symbols:

```
3x3 WCA Scramble                           3x3
2x2 WCA Scramble                           2x2
4x4 WCA Scramble                           4x4
5x5 WCA Scramble                           5x5
6x6 WCA Scramble                           6x6
7x7 WCA Scramble                           7x7
Pyraminx Scramble                          PYRAMINX
Megaminx Scramble                          MEGAMINX
Square-1 Scramble                          SQUARE ONE
Skewb Scramble                             SKEWB
Clock scramble                             CLOCK
Last Layer Scramble                        LAST LAYER
First 2 Layers Scramble                    FIRST 2 LAYERS
<MU>-Last Six Edges Scramble               LAST SIX EDGES
<RU>-gen Scramble                          RU SCRAMBLE
Last Slot and Last Layer Scramble          LAST SLOT AND LAST LAYER
[Stopwatch]                                STOPWATCH
[Print Help]                               HELP
[Quit]                                     QUIT
```

You can press `tab` to scroll through the symbols at the prompt, and arrow keys scroll through history (stored at `~/.scramble_history.txt`. You can change this location by setting the `SCRAMBLE_HISTORY` environment variable describing a different path.)

After selecting a scramble, you may repeatedly press `return`/`enter` to generate another scramble of the same type, or enter a number to generate that many scrambles of the selected type; e.g. `3x3 3`

Use Ctrl+C or Ctrl+D, or type `QUIT` to quit

The `STOPWATCH` command will start a stopwatch that stops when any key is pressed. You can use the `-H` flag when starting `cube-scramble-cli` to hide the timer while solving.

If you provide 'user input' as command line arguments, its prints the results and exits without entering interactive mode:

```
$ cube-scramble-cli 3x3 3
R' B2 L2 F2 D2 B2 R U2 R' F2 R' U' R B' R2 U2 F' L D R2
U2 B2 L2 F2 U L2 D' F2 D' U B R B U' R' U B D L'
D' R' U F2 L' U2 L F' U' D B2 U L2 B2 D' L2 B2 U' F2 R
```

This is also accessible through `python3 -m cube_scramble_cli`

###### Tests

`python3 -m doctest cube_scramble_cli/scramble_cli.py`
