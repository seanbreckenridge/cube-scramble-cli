#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cube_scramble_cli.constants import *


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
