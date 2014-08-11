#!/usr/bin/env python3

import time
from tinydb import TinyDB, where

db = TinyDB('my_diet.json')


class Meal(object):
    def __init__(self, name, cals, fat, carbs, protein, date):
        self.name = name
        self.cals = cals
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        if date:
            self.date = date
        else:
            dt = time.time()
            dt = round(time.mktime(dt)/84000)
            self.date = dt


def log_diet(name, cals, fat, carbs, protein, date):
    dt = time.strptime(date, "%m/%d/%Y")
    dt = round(time.mktime(dt)/86400)  # number of days since the epoch
    meal = {'name': name,
            'cals': cals,
            'fat': fat,
            'carbs': carbs,
            'protein': protein}
    db.insert({'date': dt, 'meal': meal})


def get_data(start, end):
    start = int(time.mktime(time.strptime(start, "%m/%d/%Y")))
    start /= 86400
    end = int(time.mktime(time.strptime(end, "%m/%d/%Y")))
    end /= 86400

    data = db.search((where('date') >= start) & (where('date') <= end))
    return data
