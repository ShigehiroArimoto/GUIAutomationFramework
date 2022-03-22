import subprocess
import PySimpleGUI as sg
import sys

sg.theme('Light Blue 2')   # デザインテーマ

layout = [ [sg.Text("Test Script",size=(8,1)),sg.Input(key="script_file"),sg.FileBrowse(key="script_file")],
           [sg.Text("Test Data",size=(8,1)),sg.Input(key="testdata_file"),sg.FileBrowse(key="testdata_file")],
           [sg.Button('EXECUTE'),sg.Button('CANCEL')]]

window = sg.Window('GUIAutomationLauncher',layout) # ウィンドウの生成

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'CANCEL':
        break
    elif event == 'EXECUTE':
        subprocess.Popen([sys.executable, values['script_file'],values['testdata_file']])   # sys.executable : pythonインタプリタのパス
        break

window.close()