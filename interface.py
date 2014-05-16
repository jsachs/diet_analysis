#!/usr/bin/env python3

import curses
import time
import visualize
import logging


def display_data_menu(screen):

    x = 0
    y = 0

    screen.clear()
    screen.border(0)

    x = get_date(screen, 2, 2, "Enter start date:")
    y = get_date(screen, 3, 2, "Enter end date:")

    curses.endwin()

    visualize.plot_diet(start=x, end=y)


def display_log_menu(screen):

    screen.clear()
    screen.border(0)

    name = get_name(screen, 2, 2, "Enter meal name:")
    cals = get_macro(screen, 3, 2, "Calories (g):")
    fat = get_macro(screen, 4, 2, "Fat (g):")
    carbs = get_macro(screen, 5, 2, "Carbs (g):")
    protein = get_macro(screen, 6, 2, "Protein (g):")
    date = get_date(screen, 7, 2, "Enter date <MM/DD/YYYY>:")

    curses.endwin()

    logging.log_diet(name, cals, fat, carbs, protein, date)


def get_name(screen, x, y, s):
    screen.addstr(x, y, s)
    while True:
        screen.addstr(x, len(s)+3, " "*60)
        name = screen.getstr(x, len(s)+3, 60)
        try:
            name = str(name)
            break
        except ValueError:
            screen.addstr(x+2, y, "Please enter a valid string")
            continue
    screen.addstr(x+2, y, " "*60)
    return name


def get_macro(screen, x, y, s):
    screen.addstr(x, y, s)
    while True:
        screen.addstr(x, len(s)+3, " "*60)
        macro = screen.getstr(x, len(s)+3, 60)
        try:
            macro = int(macro)
            break
        except ValueError:
            screen.addstr(x+2, y, "Please enter an integer")
            continue
    screen.addstr(x+2, y, " "*60)
    return macro


def get_date(screen, x, y, s):
    screen.addstr(x, y, s)
    while True:
        screen.addstr(x, len(s)+3, " "*60)
        date = screen.getstr(x, len(s)+3, 60)
        try:
            time.strptime(date, "%m/%d/%Y")
            break
        except ValueError:
            screen.addstr(x+2, y, "Please enter an integer")
            continue
    screen.addstr(x+2, y, " "*60)
    return macro


def menu_loop_wrapper():
    curses.wrapper(menu_loop)
def menu_loop(screen):
    curses.echo()
    x = 0

    while x != ord('4'):
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, "Choose an option:")
        screen.addstr(4, 4, "1 - Display data")
        screen.addstr(5, 4, "2 - Log data")
        screen.addstr(6, 4, "3 - Analysis") # Future option
        screen.addstr(7, 4, "4 - Exit")
        screen.refresh()

        x = screen.getch()

        if x == ord('1'):
            display_data_menu(screen)

        if x == ord('2'):
            display_log_menu(screen)

        if x == ord('3'):
            pass

    curses.endwin()
