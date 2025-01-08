
# Key Logger

The Keylogger Project is a simple yet effective tool designed to log keystrokes on a computer. This project captures all keystrokes made by the user and logs them into a file. In the future, it may include a Flask-based server to which the log file can be sent for remote monitoring. This project demonstrates key aspects of cybersecurity, specifically in the area of monitoring and logging user activity, and can be useful for educational purposes or as a component in larger security systems.


## Features

- Keystroke Logging: Captures all keystrokes made by the user in real-time.
- File Logging: Stores the captured keystrokes in a specified log file for later review.
- Background Operation: Runs silently in the background, ensuring minimal disruption to the user.


## Purpose
The primary purpose of this keylogger project is to provide a tool for educational purposes in the field of cybersecurity. It can be used to demonstrate the potential security risks posed by keyloggers, as well as to teach methods for detecting and preventing such threats. Additionally, it serves as a practical example of Python programming. Future enhancements may include network communication features using Flask.
## Installation

Prerequisites
- python 3.12.4 (latest version)

```bash
# Clone the repository
  git clone https://github.com/stubrish/Key-Logger

# Navigate to the project directory
  cd keylogger

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip install -r Requirement.txt
```
    
## Creating an Executable
To convert the Python file into an executable, you can use PyInstaller. Follow these steps:
- Install PyInstaller
```bash
pip install pyinstaller
```
- Generate the Executable
```bash
pyinstaller --onefile keylogger.py
```
- Locate the Executable:
The generated executable will be located in the dist folder within your project directory.

## Conclusion
Thank you for exploring the Keylogger Project! We hope this tool provides valuable insights into keystroke logging and cybersecurity.

## Summary
- Installation: Follow the provided steps to set up the project and its dependencies.
- Usage: Learn how to run the keylogger and generate an executable.
- Feedback: Share your feedback or contribute to the project by reporting issues or suggesting improvements.

## Additional Resources
- https://www.python.org/downloads/windows/
- https://docs.python.org/3/library/index.html

# Disclaimer
Please use this project responsibly and only in environments where you have explicit permission. Unauthorized use of keyloggers is illegal and unethical. The Keylogger Project is intended for educational purposes and should not be used for malicious activities.

