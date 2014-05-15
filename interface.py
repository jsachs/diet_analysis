#!/usr/bin/env python3

import curses
import visualize
import logging

#screen = curses.initscr()


def display_data_menu(screen):

    x = 0
    y = 0

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Enter start date:")
    x = screen.getstr(3, 2, 60)
    screen.addstr(4, 2, "Enter end date:")
    y = screen.getstr(5, 2, 60)

    curses.endwin()

    visualize.plot_diet(start=x, end=y)


def display_log_menu(screen):

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Enter meal name:")
    name = screen.getstr(3, 2, 60)
    screen.addstr(4, 2, "Calories (g):")
    cals = int(screen.getstr(5, 2, 60))
    screen.addstr(6, 2, "Fat (g):")
    fat = int(screen.getstr(7, 2, 60))
    screen.addstr(8, 2, "Carbs (g):")
    carbs = int(screen.getstr(9, 2, 60))
    screen.addstr(10, 2, "Protein (g):")
    protein = int(screen.getstr(11, 2, 60))
    screen.addstr(12, 2, "Enter date <DD/MM/YYYY>:")
    date = screen.getstr(13, 2, 60)

    curses.endwin()

    logging.log_diet(name, cals, fat, carbs, protein, date)


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
