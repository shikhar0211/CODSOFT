import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 8:
            raise ValueError("Length must be greater than 8")
        
        strength = strength_var.get()
        characters = ''
        if strength == 'Easy':
            characters = string.ascii_lowercase + string.ascii_uppercase
        elif strength == 'Medium':
            characters = string.ascii_letters + string.digits
        elif strength == 'Hard':
            characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for i in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")
root.geometry("550x550")
root.configure(bg='lightblue')

length_label = tk.Label(root, text="Enter password length:", bg='lightblue')
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=10)

strength_label = tk.Label(root, text="Select password strength:", bg='lightblue')
strength_label.pack(pady=10)

strength_var = tk.StringVar(root)
strength_var.set('Easy')

easy_radio = tk.Radiobutton(root, text="Easy", variable=strength_var, value='Easy', bg='lightblue')
easy_radio.pack(pady=5)

medium_radio = tk.Radiobutton(root, text="Medium", variable=strength_var, value='Medium', bg='lightblue')
medium_radio.pack(pady=5)

hard_radio = tk.Radiobutton(root, text="Hard", variable=strength_var, value='Hard', bg='lightblue')
hard_radio.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='lightgreen')
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:", bg='lightblue')
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=20)
password_entry.pack(pady=10)

root.mainloop()
