import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# -------- GUI SETUP --------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length:").pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Checkboxes
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters (A-Z)", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack()

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

# Output Password
password_entry = tk.Entry(root, width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()