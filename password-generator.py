import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        password_length = int(password_length_entry.get())
        if password_length <= 0:
            password_result_label.config(text="Password length must be a positive integer.")
            return

        password = generate_password(password_length)
        password_result_label.config(text="Generated Password: " + password)

    except ValueError:
        password_result_label.config(text="Invalid input. Please enter a valid integer for password length.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and configure the input frame
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
input_frame.columnconfigure(1, weight=1)

password_length_label = ttk.Label(input_frame, text="Password Length:")
password_length_label.grid(column=0, row=0, sticky=tk.W)

password_length_entry = ttk.Entry(input_frame)
password_length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
password_length_entry.insert(0, "0")

generate_password_button = ttk.Button(input_frame, text="Generate Password", command=generate_password_button_click)
generate_password_button.grid(column=0, row=1, columnspan=2)

# Create and configure the result label
password_result_label = ttk.Label(root, text="", padding=10)
password_result_label.grid(column=0, row=1)

# Start the main loop
root.mainloop()
