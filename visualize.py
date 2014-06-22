#!usr/bin/env python3

import analyze
import logging
import numpy as np
import matplotlib.pyplot as plot


def plot_diet(start, end):

    data = logging.get_data(start, end)
    cals, fat, carbs, protein, dates = analyze.get_macros(data)

    for l in (cals, fat, carbs, protein, dates):
        l = np.array(l)

    # Arrange graph dimensions
    N = len(dates)
    ind = np.arange(N) + 0.3  # the x locations for the groups
    width = 0.4               # the width of the bars

    # Initialize figure
    fig = plot.figure()

    # Set up bar pieces
    p1 = plot.bar(ind, fat, width, color="green")
    p2 = plot.bar(ind, carbs, width, color="blue", bottom=fat)
    p3 = plot.bar(ind, protein, width, color="red", bottom=np.add(carbs,fat))

    # Set up graph labels
    plot.ylabel('Calories')
    plot.title('Calories by macronutrient', y = 1.05)
    plot.xticks(ind+width/2., format_labels(dates))
    plot.yticks(np.arange(0,5000,500))

    # Set up graph legend
    lgd = plot.legend([p1, p2, p3], ["Fat", "Carbs", "Protein"],
                      loc='upper center',
                      bbox_to_anchor=(0.5, 1.05),
                      ncol=3,
                      fancybox=True,
                      shadow=True)

    plot.show()

def format_labels(dates):
    ret = []
    for date in dates:
        date = date[:-5]
        ret.append(date)
    return ret
