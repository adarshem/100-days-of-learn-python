import platform
import os

# Function to clear the terminal
def clear_terminal():
    """
    Clears the terminal/command line across different platforms.
    Uses a fallback method if the standard commands are unavailable.
    """
    try:
        if platform.system() != "Windows":
            # Set TERM if not already defined
            if not os.getenv("TERM"):
                os.environ["TERM"] = "xterm-256color"

            # Attempt to clear for macOS/Linux
            result = os.system('clear')
        else:
            # Attempt to clear for Windows
            result = os.system('cls')

            # Fallback if the command fails
        if result != 0:
            raise OSError("System command failed")
    except Exception:
        # Fallback in case the system commands are unavailable
        print("\n" * 100)