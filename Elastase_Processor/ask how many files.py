import PySimpleGUI as sg
import tkinter as tk

#### 00 get input files from user
sg.change_look_and_feel('Topanga')  ### my GUI colourful setting

layout1 = [
    [sg.Text('Number of input files: '), sg.Input()],
    [sg.OK(), sg.Cancel()]
]
######Display first window to ask how many input files
window = sg.Window('Protease Processor', layout1)
event, Number_input_files = window.Read()
Number_questions_to_ask = Number_input_files[0]

Number_questions_to_ask = int(Number_questions_to_ask)
text = ''
x = 0
while x != Number_questions_to_ask:

    text += f'[sg.Text(CSV file {x+1}: )), sg.Input(), sg.FileBrowse()],\n'

    x += 1

while x != Number_questions_to_ask:
    text=tk.StringVar()
    x += 1

print(text)

layout2 = [
    text,
    [sg.Text('Select output path'), sg.Input(), sg.FolderBrowse()],
    [sg.OK(), sg.Cancel()]
]


window = sg.Window('Protease Processor', layout2)
event, inp = window.Read()
print(inp)