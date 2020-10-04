# -*- coding: utf-8 -*-

import curses
from time import perf_counter

def format_time(seconds: float) -> str:
    """Formats time into mm:ss:xx"""
    minutes, seconds = divmod(seconds, 60)
    centi = "{:.2f}".format(seconds % 1)[1:]
    return "{:02d}:{:02d}{}".format(int(minutes), int(seconds), centi)


def run(stdscr, start_time: float, show_text: bool) -> str:  # type: ignore[no-untyped-def]
    curses.echo()  # allow character input
    stdscr.timeout(0)  # non blocking
    while True:
        if show_text:
            stdscr.addstr(5, 10, format_time(perf_counter() - start_time))
        if stdscr.getch() != -1:
            return format_time(perf_counter() - start_time)


def stopwatch(hide_text: bool = False) -> str:
    return curses.wrapper(run, perf_counter(), not hide_text)
