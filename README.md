# KeyLogger

This project is a simple **Python-based keylogger** built using Windows APIs and `pyWinhook`. It captures all keystrokes and logs them into a text file.

> ⚠️ **Disclaimer**: This project is strictly for **educational** and **personal testing** purposes. Unauthorized keylogging is **illegal** and unethical. Use responsibly.

---

You need the following Python packages (Windows only):

- `pyWinhook`
- `pythoncom` (comes with `pywin32`)
- `pywin32`


  ## 💻 How It Works

1. **Hides the console window** so it runs silently in the background.
2. **Hooks into the keyboard input** using `pyWinhook`.
3. **Captures every key pressed**, converting it to a readable character.
4. **Appends to a local log file**.
5. Exits cleanly when the user presses `Ctrl + E` (ASCII 5).
