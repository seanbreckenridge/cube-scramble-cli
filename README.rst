=================
cube scramble cli
=================

|ver_no| |py_ver|

.. |ver_no| image:: https://img.shields.io/pypi/v/cube_scramble_cli.svg
        :target: https://pypi.python.org/pypi/cube_scramble_cli

.. |py_ver| image:: https://img.shields.io/pypi/pyversions/cube_scramble_cli.svg
        :target: https://pypi.python.org/pypi/cube_scramble_cli


A simple CLI for pyTwistyScrambler_, to generate random states for twisty puzzles.

Installation
--------

::

    $ python3 -m pip install cube-scramble-cli

Run
--------

::

    $ cube-scramble-cli

Supported Symbols:

::

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
  [Quit]                                     QUIT

After selecting a scramble, you may repeatedly press ``return``/``enter``
to generate another scramble of the same type.
You can generate multiple scrambles of the same type,
by providing a number after a symbol; e.g. ``3x3 3``

Use Ctrl+C or Ctrl+D, or type ``QUIT`` to quit

.. _pyTwistyScrambler: https://github.com/euphwes/pyTwistyScrambler
.. _prompt_toolkit: https://github.com/prompt-toolkit/python-prompt-toolkit
