#
#  Open a terminal, navigate to the folder this file is in.
#  Enter 'python duckyscript_simulator.py' in your terminal and press ENTER.
#  To change your script, simply edit the code at the bottom!
#  Be mindful of what you do to your machine!
#  Remember not to cause any harm, for education purposes only!
#  


import time
import pyautogui

print(pyautogui.__version__)


def execute_duckyscript(duckyscript):
    lines = duckyscript.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Wait for a moment before executing the next line
        time.sleep(0.5)

        # Split the line into command and arguments
        command, *args = line.split()

        if command == "DELAY":
            # DELAY command
            delay_time = int(args[0])
            time.sleep(delay_time / 1000.0)
        elif command == "STRING":
            # STRING command
            text = ' '.join(args)
            pyautogui.typewrite(text)
        elif command == "REM":
            # REM command, comment, do nothing
            pass
        elif command == "DELAY_AFTER":
            # DELAY_AFTER command
            delay_time = int(args[0])
            time.sleep(delay_time / 1000.0)
        elif command == "REPEAT":
            # REPEAT command
            repeat_count = int(args[0])
            for _ in range(repeat_count):
                execute_duckyscript(' '.join(args[1:]))
        elif command == "REPEAT_END":
            # REPEAT_END command
            pass  # No action needed, handled in REPEAT
        elif command == "ENTER":
            # ENTER command
            pyautogui.press('enter')
        elif command == "TAB":
            # TAB command
            pyautogui.press('tab')
        elif command == "ESC":
            # ESC command
            pyautogui.press('esc')
        elif command == "CONTROL" or command == "CTRL":
            # CONTROL/CTRL command
            pyautogui.press('ctrl')
        elif command == "ALT":
            # ALT command
            pyautogui.press('alt')
        elif command == "SHIFT":
            # SHIFT command
            pyautogui.press('shift')
        elif command == "GUI" or command == "WINDOWS":
            # GUI/Windows key command
            pyautogui.press('winleft')
        elif command == "APP" or command == "MENU":
            # APP/MENU key command
            pyautogui.press('apps')
        elif command == "UP" or command == "DOWN" or command == "LEFT" or command == "RIGHT":
            # Arrow key commands
            pyautogui.press(command.lower())
        elif command == "UPARROW" or command == "DOWNARROW" or command == "LEFTARROW" or command == "RIGHTARROW":
            # Arrow key commands
            pyautogui.press(command.lower().replace('arrow', ''))
        elif command == "CAPSLOCK":
            # CAPSLOCK command
            pyautogui.press('capslock')
        elif command == "PRINTSCREEN":
            # PRINTSCREEN command
            pyautogui.press('printscreen')
        elif command == "SCROLLLOCK":
            # SCROLLLOCK command
            pyautogui.press('scrolllock')
        elif command == "NUMLOCK":
            # NUMLOCK command
            pyautogui.press('numlock')
        elif command == "HOME":
            # HOME command
            pyautogui.press('home')
        elif command == "END":
            # END command
            pyautogui.press('end')
        elif command == "PAGEUP":
            # PAGEUP command
            pyautogui.press('pageup')
        elif command == "PAGEDOWN":
            # PAGEDOWN command
            pyautogui.press('pagedown')
        elif command == "DELETE":
            # DELETE command
            pyautogui.press('delete')
        elif command == "INSERT":
            # INSERT command
            pyautogui.press('insert')
        elif command == "F1" or command == "F2" or command == "F3" or command == "F4" or command == "F5" \
                or command == "F6" or command == "F7" or command == "F8" or command == "F9" or command == "F10" \
                or command == "F11" or command == "F12":
            # Function key commands
            pyautogui.press(command.lower())
        elif command == "SPACE":
            # SPACE command
            pyautogui.press('space')
        else:
            print(f"Unsupported command: {command}")


if __name__ == "__main__":
    # Example Duckyscript
    duckyscript_example = """
DELAY 500
WINDOWS
DELAY 500
STRING run
DELAY 200
ENTER
DELAY 2500
STRING cmd
DELAY 200
ENTER
DELAY 2500
STRING tree
DELAY 200
ENTER
    """

    execute_duckyscript(duckyscript_example)
