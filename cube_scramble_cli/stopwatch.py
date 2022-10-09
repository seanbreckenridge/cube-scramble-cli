import curses
from time import perf_counter


def format_time(seconds: float, decimals: int) -> str:
    """Formats time into mm:ss:xx"""
    minutes, seconds = divmod(seconds, 60)
    fmt_string = f"{{:.{decimals}f}}"
    centi = fmt_string.format(seconds % 1)[1:]
    return "{:02d}:{:02d}{}".format(int(minutes), int(seconds), centi)


def run(
    stdscr: curses.window, start_time: float, show_text: bool, decimals: int
) -> str:
    curses.echo()  # allow character input
    stdscr.timeout(0)  # non blocking
    while True:
        if show_text:
            stdscr.addstr(
                5, 10, format_time(perf_counter() - start_time, decimals=decimals)
            )
        if stdscr.getch() != -1:
            return format_time(perf_counter() - start_time, decimals=decimals)


def stopwatch(hide_text: bool = False, decimals: int = 2) -> str:
    return curses.wrapper(run, perf_counter(), not hide_text, decimals)
