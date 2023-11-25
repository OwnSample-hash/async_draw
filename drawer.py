import _curses, curses
import curses.panel
from typing import Dict

TIME_IT_STAT_NS = {}

def main(stdscr: _curses.window, timeit_ns: Dict[str, int]):
    TIME_IT_STAT_NS = timeit_ns
    stdscr.clear()
    stdscr.box()
    stdscr.refresh()
    key = ""
    while True:
        key = stdscr.getkey()
        x, y = curses.COLS, curses.LINES
        match (key):
            case "t":
                stats = len(TIME_IT_STAT_NS)
                timings_w = curses.newwin(
                    stats + 5,
                    int(x / 4),
                    int((y / 2) - (stats + 5) / 2),
                    int(x / 2-(x/8))
                )
                timings_p = curses.panel.new_panel(timings_w)
                i = 2
                timings_w.box()
                timings_w.addstr(1, int((y / 2) - (stats) / 2-2), "Timings")
                for k, v in TIME_IT_STAT_NS.items():
                    timings_w.addstr(i, 1, f"Stat {k} took {v} ns")
                    i += 1
                timings_w.addstr(i+1, int((y / 2) - (stats) / 2-5), "Press q to close")
                timings_w.refresh()
                while True:
                    if timings_w.getkey() == 'q':
                        break
                timings_p.hide()
            case "q":
                break
            case "Q":
                break
            case _:
                pass

        pass
