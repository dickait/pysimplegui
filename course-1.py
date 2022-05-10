import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'), 
        sg.Spin(['km to mile', 'kg to pound', 'sec to min', 'celcius to fahreinheit'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output:', key='-OUTPUT-'), sg.Text('', key='-OUTPUT-TEXT-')],
]

window = sg.Window('Converter').Layout(layout)

while True:
    event, values = window.Read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            if values['-UNITS-'] == 'km to mile':
                output = round(float(input_value) * 0.621371, 2)
                output_string = f'{input_value} km is {output} miles'
            elif values['-UNITS-'] == 'kg to pound':
                output = round(float(input_value) * 2.20462, 2)
                output_string = f'{input_value} kg is {output} pounds'
            elif values['-UNITS-'] == 'sec to min':
                output = round(float(input_value) / 60, 2)
                output_string = f'{input_value} sec is {output} min'
            elif values['-UNITS-'] == 'celcius to fahreinheit':
                output = round(float(input_value) * 1.8 + 32, 2)
                output_string = f'{input_value} celcius is {output} fahreinheit'
        window['-OUTPUT-TEXT-'].Update(output_string)         

window.close()