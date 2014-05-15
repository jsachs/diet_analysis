#!/usr/bin/env python3

import time
from tinydb import TinyDB, where

db = TinyDB('my_diet.json')


def log_diet(name, cals, fat, carbs, protein, date):
    dt = time.strptime(date, "%m/%d/%Y")
    dt = time.mktime(dt)/86400 # number of days since the epoch
    meal = {'name': name,
            'cals':cals,
            'fat': fat,
            'carbs': carbs,
            'protein': protein
    }
    db.insert({'date': time.mktime(dt), 'meal': meal})


def get_data(start, end):
    start = int(time.mktime(time.strptime(start, "%m/%d/%Y")))
    start = start/86400
    end = int(time.mktime(time.strptime(end, "%m/%d/%Y")))
    end = end/86400

    data = db.search((where('date') >= start) & (where('date') <= end))
    return data


def dict_merge(target, *args):
    # Merge multiple dicts
    if len(args) > 1:
        for obj in args:
            dict_merge(target, obj)
        return target

    # Recursively merge dicts and set non-dict values
    obj = args[0]
    if not isinstance(obj, dict):
        return obj
    for k, v in obj.iteritems():
        if k in target and isinstance(target[k], dict):
            dict_merge(target[k], v)
        else:
            target[k] = deepcopy(v)
        return target
