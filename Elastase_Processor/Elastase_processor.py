#!/usr/bin/env python

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

import PySimpleGUI as sg

# #### I want to convert the next into a manual entry for WT candidate locations

# #### 00 get input file from user
# sg.change_look_and_feel('Topanga')  ### my GUI colourful setting
#
# layout = [
#     [sg.Text('Select a .csv file)'), sg.Input(), sg.FileBrowse()],
#     [sg.Text('Select output path'), sg.Input(), sg.FolderBrowse()],
#     [sg.OK(), sg.Cancel()]
# ]
#
# window = sg.Window('Protease Processor', layout)
# event, inp = window.Read()
# print(inp)

#### 01 format the input file to remove all the rows at the beginning of the file that aren't part of the data frame
with open('Elastase_InputFile.csv', 'rt') as inp:
    with open('Elastase_CleanedFile.csv', 'wt') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if len(row) > 3:
                writer.writerow(row)

#### exclude the ladder values in Lane 1 from dataframe
df = pd.read_csv('Elastase_CleanedFile.csv')
df2 = df.loc[df['Lane'] > 1]

#### 02 calculate percentage of degradation between neighbouring lanes
no_protease_value, with_protease_value, pair_number = 0.0, 0.0, 0.0
list_of_values, list_no_protease_values, list_with_protease_values, degradation_percentages = [], [], [], []
for row in range(2, len(df2) + 2):
    if row % 2 == 0:
        no_protease_value = float(df2.loc[df2['Lane'] == row, 'Volume'].values)
        list_no_protease_values.append(no_protease_value)
        list_of_values.append(no_protease_value)
    if row % 2 == 1:
        pair_number += 1
        with_protease_value = float(df2.loc[df2['Lane'] == row, 'Volume'].values)
        list_of_values.append(with_protease_value)
        list_with_protease_values.append(with_protease_value)
        degradation_percentages.append(round(100 * with_protease_value / no_protease_value))

####03 get the 96 candidate names
from candidate_names import candidates

candidate_names = candidates()

### 04 SORT THE CANDIDATE NAMES AND DEGRADATION PERCENTAGE VALUES

sorted_CandNames_and_DegPercent = list(zip(candidate_names, degradation_percentages))
sorted_CandNames_and_DegPercent = sorted(sorted_CandNames_and_DegPercent, key=lambda tup: tup[1], reverse=True)

sorted_CandNames, sorted_DegPercent = [], []
for x in range(len(sorted_CandNames_and_DegPercent)):
    sorted_CandNames.append(sorted_CandNames_and_DegPercent[x][0])
    sorted_DegPercent.append(sorted_CandNames_and_DegPercent[x][1])


### 05 PLOTTING THE BAR CHART
x = np.arange(len(sorted_CandNames))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width * 1.2 / 2, list_no_protease_values, width, label='– Protease')
rects2 = ax.bar(x + width * 1.2 / 2, list_with_protease_values, width, label='+Protease')

#### Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Band intensity')
ax.set_title('Raw Densitometry')
ax.set_xticks(x)
ax.set_xticklabels(list(candidate_names))
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.savefig('Band intensities')

#### display graph with percentages of degradation
x2 = np.arange(len(sorted_CandNames))  # the label locations
width2 = 0.2  # the width of the bars

fig2, ax = plt.subplots()
rects3 = ax.bar(x2, sorted_DegPercent, width2)

#### Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% intact')
ax.set_title('Protease stability')
ax.set_xticks(x2)
ax.set_xticklabels(list(sorted_CandNames))


def autolabel2(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel2(rects3)

fig2.tight_layout()

plt.savefig('Protease stabilities')

os.remove("Elastase_CleanedFile.csv")