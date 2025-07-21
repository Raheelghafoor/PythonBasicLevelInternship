#problem 20 (sheet 2)

import tkinter as tk
from tkinter import messagebox

# Functions for each menu action
def add_numbers():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        result_label.config(text=f"Sum = {a + b}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

def subtract_numbers():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        result_label.config(text=f"Difference = {a - b}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

def exit_app():
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("Simple Python Menu GUI")
root.geometry("300x250")

# Labels and input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Menu buttons
tk.Button(root, text="Add", command=add_numbers).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_numbers).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
