#!/bin/env python3
from curses import wrapper
from drawer import main
from typing import Dict
from data_in.lexer import Lexer
from data_in.parser import Parser
from typing import List
from time import perf_counter_ns
from pprint import pp


def gen_empty_vars():
    return {
        "x1": False,
        "x2": True,
        "y1": True,
        "y2": True,
    }


def dec2anys(num: int, pad: int, base: int = 2) -> str:
    outs = ""
    while 1:
        outs += str(num % base)
        num = int(str(num / base).split(".")[0])
        if num == 0:
            break
    outs = outs[::-1]
    if len(outs) < pad:
        diff = pad - len(outs)
        outs = "0" * diff + outs
    return outs


LOOKUP_LIST: List[str] = [
    "x1",
    "x2",
    "y1",
    "y2",
]


def get_next_vars(p_index: int) -> Dict[str, bool]:
    out: Dict[str, bool] = {
        "x1": False,
        "x2": False,
        "y1": False,
        "y2": False,
    }
    i = 0
    for char in dec2anys(p_index, 4):
        if char == "1":
            out[LOOKUP_LIST[i]] = True
        i += 1
    return out


def read_in(fn: str) -> str:
    try:
        with open(fn) as f:
            out = f.readline()
    except FileNotFoundError:
        out = input(f"{fn.upper()}=")
    return out


TIME_IT_STAT_NS = {}

if __name__ == "__main__":
    # print('Possilbe valuse are y1 y2 x1 x2 + () ! in minterm form')
    start_read_in = perf_counter_ns()
    Z = read_in("z")
    Y1 = read_in("y2")
    Y2 = read_in("y2")
    TIME_IT_STAT_NS["read_in"] = perf_counter_ns() - start_read_in

    start_z_ = perf_counter_ns()
    for i in range(0, 16):
        vars = get_next_vars(i)
        lex = Lexer(Z)
        parser = Parser(lex, vars)
        res = parser.expr()
        # f.write(f'{i}, {res}\n')
        if i == 15:
            break
    TIME_IT_STAT_NS["z"] = perf_counter_ns() - start_z_

    start_y1_ = perf_counter_ns()
    for i in range(0, 16):
        vars = get_next_vars(i)
        lex = Lexer(Y1)
        parser = Parser(lex, vars)
        res = parser.expr()
        # f.write(f'{i}, {res}\n')
        if i == 15:
            break
    TIME_IT_STAT_NS["y1"] = perf_counter_ns() - start_y1_

    start_y2_ = perf_counter_ns()
    for i in range(0, 16):
        vars = get_next_vars(i)
        lex = Lexer(Y1)
        parser = Parser(lex, vars)
        res = parser.expr()
        # f.write(f'{i}, {res}\n')
        if i == 15:
            break
    TIME_IT_STAT_NS["y2"] = perf_counter_ns() - start_y2_

    pp(TIME_IT_STAT_NS)
    wrapper(main, TIME_IT_STAT_NS)
