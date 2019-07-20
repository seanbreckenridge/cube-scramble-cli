# -*- coding: utf-8 -*-

import curses
from time import clock

def format_time(seconds):
    """Formats time into mm:ss:xx"""
    minutes, seconds = divmod(seconds, 60)
    centi = "{:.2f}".format(seconds % 1)[1:]
    return "{:02d}:{:02d}{}".format(int(minutes), int(seconds), centi)


def run(stdscr, start_time, show_text):
    curses.echo()  # allow character input
    stdscr.timeout(0)  # non blocking
    while True:
        if show_text:
            stdscr.addstr(5, 10, format_time(clock() - start_time))
        if stdscr.getch() != -1:
            return format_time(clock() - start_time)


def stopwatch(hide_text=False):
    return curses.wrapper(run, clock(), not hide_text)
