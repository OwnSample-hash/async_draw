#!/bin/env python3
from curses import wrapper
import _curses

from data_in.lexer import Lexer
from data_in.parser import Parser


def main(stdscr: _curses.window):
    stdscr.clear()
    stdscr.addstr(0, 0, str(type(stdscr)))
    stdscr.refresh()
    stdscr.getkey()


def gen_empty_vars():
    return {
        'x1': False,
        'x2': True,
        'y1': True,
        'y2': True,
    }


if __name__ == '__main__':
    print('Possilbe valuse are y1 y2 x1 x2 + () !')
    try:
        with open('z') as f:
            z = f.readline()
            print("Read from './z' file")
    except FileNotFoundError:
        print("'./z' file was not found")
        z = input('Z=')
    lex = Lexer(z)
    vars = gen_empty_vars()
    print(vars)
    parser = Parser(lex, vars)
    res = parser.expr()
    print(res)

    # wrapper(main)
