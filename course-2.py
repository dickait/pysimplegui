import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
            [sg.Text('Output', font= 'Franklin 26', justification = 'right', expand_x = True, pad = (10,20), right_click_menu=list_theme ,  key='-OUTPUT-')],
            [sg.Button('Clear', expand_x=True, key='-CLEAR-'), sg.Button('Enter', expand_x=True, key='-ENTER-')],
            [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('/', size = button_size)],
            [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('*', size = button_size)], 
            [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
            [sg.Button(0, expand_x=True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)],
        ]
    return sg.Window('Calculator', layout)

list_theme = ['menu',['Default', 'Dark Blue', 'Dark Green', 'Dark Red', 'Dark Purple', 'Light Blue', 'Light Green', 'Light Red', 'Light Purple']]
window = create_window('dark')

current_num = []
full_operation = []

while True:
    event, values = window.Read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event in list_theme[1]:
        window.close
        window = create_window(event)
    
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_str = ''.join(current_num)
        window['-OUTPUT-'].Update(num_str)
        print(num_str)
        
    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-OUTPUT-'].Update()
        
    if event == '-ENTER-':
        full_operation.append(''.join(current_num))
        print(full_operation)
        result = eval(''.join(full_operation))
        window['-OUTPUT-'].Update(result)
        full_operation = []
        
    if event == '-CLEAR-':
        current_num = []
        full_operation = []
        window['-OUTPUT-'].Update('')
        
window.close()