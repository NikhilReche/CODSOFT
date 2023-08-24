import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showerror("Invalid Length", "Password length must be at least 4 characters.")
        return

    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("No Characters Selected", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#545450")



length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_label.configure(bg="#ffc07d")
length_var = tk.IntVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()
length_var.set(12)  
length_entry.configure(bg="#f3f59d")


lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var)
lowercase_check.pack()
lowercase_var.set(True)  
lowercase_check.configure(bg="#e3a6da")

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
uppercase_check.pack()
uppercase_var.set(True)  
uppercase_check.configure(bg="#e3a6da")

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var)
digits_check.pack()
digits_var.set(True)  
digits_check.configure(bg="#e3a6da")

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
special_chars_check.pack()
special_chars_check.configure(bg="#e3a6da")
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()
generate_button.configure(bg="#43fa6b")


password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_label.configure(bg="#ffc07d")
password_entry = tk.Entry(root)
password_entry.pack()
password_entry.configure(bg="#f3f59d")


root.mainloop()
