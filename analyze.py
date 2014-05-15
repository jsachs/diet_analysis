#!usr/bin/env python3

import time


"""
get_daily_calories(data, date)
Accumulates the number of calories in a single date in a diet dataset.
inputs:
    - data: json object
    - date: string representation of date <DD/MM/YYYY>
returns:
    - (int) daily number of calories
"""
def get_daily_calories(data, date):
    meals = data[date]
    cals = 0
    for m in meals:
        cals += m["cals"]
    return cals


"""
get_daily_fat(data, date)
Accumulates the amount of fat in a single date in a diet dataset.
inputs:
    - data: json object
    - date: string representation of date <DD/MM/YYYY>
returns:
    - (int) total grams of fat
"""
def get_daily_fat(data, date):
    meals = data[date]
    fat = 0
    for m in meals:
        fat += m["fat"]
    return fat


"""
get_daily_calories(data, date)
Accumulates the amount of carbs in a single date in a diet dataset.
inputs:
    - data: json object
    - date: string representation of date <DD/MM/YYYY>
returns:
    - (int) total grams of carbs
"""
def get_daily_carbs(data, date):
    meals = data[date]
    carbs = 0
    for m in meals:
        carbs += m["carbs"]
    return carbs


"""
get_daily_protein(data, date)
Accumulates the amount of protein in a single date in a diet dataset.
inputs:
    - data: json object
    - date: string representation of date <DD/MM/YYYY>
returns:
    - (int) total grams of protein
"""
def get_daily_protein(data, date):
    meals = data[date]
    protein = 0
    for m in meals:
        protein += m["protein"]
    return protein


"""
get_daily_calories(data)
Accumulates the number of calories in a single dat in a diet dataset.
inputs:
    - date: json object, chosen by date
    - item: string for cals, fat, carbs, or protein
returns:
    - (int) total number of calories
"""
def get_macros(data):
    new_data = {}
    # merge "rows" of data
    for row in data:
        if row['date'] not in new_data:
            new = []
            new.append(row['meal'])
            new_data[row['date']] = new
        else:
            new = new_data[row['date']]
            new.append(row['meal'])
            new_data[row['date']] = new

    cals, fat, carbs, protein, dates = [], [], [], [], []
    for key in sorted(new_data):
        cals.append(get_daily_calories(new_data, key))
        fat.append(9 * get_daily_fat(new_data, key))
        carbs.append(4 * get_daily_carbs(new_data, key))
        protein.append(4 * get_daily_protein(new_data, key))
        # convert date back to readable string
        date = time.strftime("%m/%d/%Y", time.gmtime(key*86400))
        dates.append(date)
    return cals, fat, carbs, protein, dates
