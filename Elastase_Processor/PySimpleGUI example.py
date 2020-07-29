import PySimpleGUI as sg

sg.change_look_and_feel('Topanga')  # please make your creations colorful

# GUI setting

labels = [
    [sg.Text('Please enter the candidate names: ')],
    [sg.Text('1', size=(15, 1)), sg.InputText()],
    [sg.Text('2', size=(15, 1)), sg.InputText()],
    [sg.Text('3', size=(15, 1)), sg.InputText()],
    [sg.Text('4', size=(15, 1)), sg.InputText()],
    [sg.Text('5', size=(15, 1)), sg.InputText()],
    [sg.Text('6', size=(15, 1)), sg.InputText()],
    [sg.Text('7', size=(15, 1)), sg.InputText()],
    [sg.Text('8', size=(15, 1)), sg.InputText()],
    [sg.Text('9', size=(15, 1)), sg.InputText()],
    [sg.Text('10', size=(15, 1)), sg.InputText()],
    [sg.Text('11', size=(15, 1)), sg.InputText()],
    [sg.Text('12', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Protease Processor', labels)
event, values = window.Read()
print(labels)
'''

layout = [[sg.Text('My one-shot window.')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered', text_input)





sg.theme('Topanga')  # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
print(event, values[0], values[1], values[2])  # the input data looks like a simple list when auto numbered
'''