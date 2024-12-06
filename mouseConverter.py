from pynput.mouse import Controller, Button
import time

def ParseHidData(dataLine):
    """
    Parse a single line of HID data.
    Each line is assumed to be 6 hex bytes in little-endian format.
    """

    rawBytes = bytes.fromhex(dataLine)

    buttonState = rawBytes[0]
    
    # Parse x and y movement from the HID data
    x = rawBytes[1] if rawBytes[1] < 128 else rawBytes[1] - 256  # Handling signed values
    y = rawBytes[2] if rawBytes[2] < 128 else rawBytes[2] - 256  # Handling signed values
    
    return buttonState, x, y

def SimulateMouseMovements(hidData):
    """
    Simulate mouse movements and button presses from a list of HID data strings.
    """
    mouse = Controller()  # Initialize the mouse controller
    
    for dataLine in hidData:
        buttonState, x, y = ParseHidData(dataLine)
        
        mouse.move(x, y)  # Move the mouse by (x, y) instantly
        
        if buttonState == 1:  # Left button pressed
            mouse.press(Button.left)
        else:  # Left button released
            mouse.release(Button.left)
        time.sleep(0.01)


with open("captures/mouse-hunt-p1.txt", "r") as file:
    hidData = [line.strip() for line in file.readlines() if line.strip()]

time.sleep(5)

SimulateMouseMovements(hidData)
