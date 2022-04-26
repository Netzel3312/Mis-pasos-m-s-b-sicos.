import PySimpleGUI as sg

print(sg.Window('app de una linea', [[sg.Input(),sg.Button('Ok'),sg.Button('Cancel')]]).read())