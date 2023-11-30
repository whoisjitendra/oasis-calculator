import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=10)
        
        self.upper_var = tk.IntVar()
        self.upper_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.upper_var)
        self.upper_checkbox.pack(pady=5)
        
        self.lower_var = tk.IntVar()
        self.lower_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lower_var)
        self.lower_checkbox.pack(pady=5)
        
        self.digit_var = tk.IntVar()
        self.digit_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.digit_var)
        self.digit_checkbox.pack(pady=5)
        
        self.symbol_var = tk.IntVar()
        self.symbol_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=self.symbol_var)
        self.symbol_checkbox.pack(pady=5)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)
        
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        character_set = ""
        if self.upper_var.get():
            character_set += string.ascii_uppercase
        if self.lower_var.get():
            character_set += string.ascii_lowercase
        if self.digit_var.get():
            character_set += string.digits
        if self.symbol_var.get():
            character_set += string.punctuation

        if not character_set:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        messagebox.showinfo("Generated Password", f"Your generated password is:\n\n{password}")

    def copy_to_clipboard(self):
        password = messagebox.askstring("Copy to Clipboard", "Enter the password to copy:")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
