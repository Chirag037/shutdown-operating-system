import os
import platform
import tkinter as tk
from tkinter import messagebox

# Function to shut down the system
def shutdown():
    confirm = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shut down?")
    if confirm:
        system_os = platform.system()
        if system_os == "Windows":
            os.system("shutdown /s /t 1")
        elif system_os == "Linux" or system_os == "Darwin":
            os.system("shutdown now")
        else:
            messagebox.showerror("Error", f"Unsupported OS: {system_os}")

# GUI setup
window = tk.Tk()
window.title("Shutdown App")
window.geometry("300x150")
window.resizable(False, False)

label = tk.Label(window, text="Click below to shutdown", font=("Arial", 12))
label.pack(pady=20)

shutdown_button = tk.Button(window, text="Shutdown", command=shutdown, bg="red", fg="white", font=("Arial", 12))
shutdown_button.pack(pady=10)

window.mainloop()
