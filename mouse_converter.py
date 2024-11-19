from pynput.mouse import Controller, Button
import time

def parse_hid_data(data_line):
    """
    Parse a single line of HID data.
    Each line is assumed to be 6 hex bytes in little-endian format.
    """
    # Convert the string into bytes
    raw_bytes = bytes.fromhex(data_line)

    # Parse button state (first byte)
    button_state = raw_bytes[0]
    
    # Parse x and y movement from the HID data
    x = raw_bytes[1] if raw_bytes[1] < 128 else raw_bytes[1] - 256  # Handling signed values
    y = raw_bytes[2] if raw_bytes[2] < 128 else raw_bytes[2] - 256  # Handling signed values
    
    return button_state, x, y

def simulate_mouse_movements_and_buttons(hid_data):
    """
    Simulate mouse movements and button presses from a list of HID data strings.
    """
    mouse = Controller()  # Initialize the mouse controller
    
    for data_line in hid_data:
        button_state, x, y = parse_hid_data(data_line)
        
        # Simulate mouse movement
        mouse.move(x, y)  # Move the mouse by (x, y) instantly
        
        # Simulate button presses/releases if the state changes
        if button_state == 1:  # Left button pressed
            mouse.press(Button.left)
        else:  # Left button released
            mouse.release(Button.left)

# HID data from the input
with open("captures/dell-mouse-ctf-1-output.txt", "r") as file:
    hid_data = [line.strip() for line in file.readlines() if line.strip()]

# Wait 2 seconds before recreating the mouse movements
time.sleep(2)

# Simulate the movements and button presses
simulate_mouse_movements_and_buttons(hid_data)
