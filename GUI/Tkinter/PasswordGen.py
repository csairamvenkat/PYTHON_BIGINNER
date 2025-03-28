import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(padx=20, pady=20)
        
        # Configure styles
        self.configure_styles()
        
        # Create widgets
        self.create_widgets()
    
    def configure_styles(self):
        # Set background color
        self.root.configure(bg="#f0f0f0")
        
        # Define colors
        self.primary_color = "#4a6ea9"
        self.secondary_color = "#ffffff"
        self.accent_color = "#ff6b6b"
    
    def create_widgets(self):
        # Title label
        title_label = tk.Label(
            self.root, 
            text="Password Generator", 
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            fg=self.primary_color
        )
        title_label.pack(pady=(0, 20))
        
        # Frame for length input
        length_frame = tk.Frame(self.root, bg="#f0f0f0")
        length_frame.pack(fill="x", pady=(0, 10))
        
        # Length label
        length_label = tk.Label(
            length_frame, 
            text="Password Length (8-15):", 
            font=("Helvetica", 10),
            bg="#f0f0f0"
        )
        length_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Length input
        self.length_var = tk.StringVar(value="8")
        self.length_entry = tk.Entry(
            length_frame, 
            textvariable=self.length_var, 
            width=5,
            font=("Helvetica", 10)
        )
        self.length_entry.pack(side=tk.LEFT)
        
        # Generate button
        generate_button = tk.Button(
            self.root, 
            text="Generate Password", 
            command=self.generate_password,
            bg=self.primary_color,
            fg=self.secondary_color,
            font=("Helvetica", 10, "bold"),
            padx=20,
            pady=5,
            borderwidth=0
        )
        generate_button.pack(pady=(10, 20))
        
        # Result frame
        result_frame = tk.Frame(self.root, bg="#f0f0f0")
        result_frame.pack(fill="x")
        
        # Result label
        result_label = tk.Label(
            result_frame, 
            text="Generated Password:", 
            font=("Helvetica", 10),
            bg="#f0f0f0"
        )
        result_label.pack(anchor="w")
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            result_frame, 
            textvariable=self.password_var, 
            width=30,
            font=("Helvetica", 12),
            readonlybackground=self.secondary_color,
            state="readonly"
        )
        password_entry.pack(fill="x", pady=(5, 10))
        
        # Copy button
        copy_button = tk.Button(
            result_frame, 
            text="Copy to Clipboard", 
            command=self.copy_to_clipboard,
            bg="#4CAF50",
            fg=self.secondary_color,
            font=("Helvetica", 10),
            padx=10,
            pady=2,
            borderwidth=0
        )
        copy_button.pack(anchor="e")
    
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            
            # Validate length
            if length < 8 or length > 15:
                messagebox.showerror("Invalid Input", "Password length must be between 8 and 15.")
                return
            
            # Define character sets
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            special_chars = "!@#$%^&*()_-+=<>?/"
            
            # Ensure at least one of each type
            password = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(special_chars)
            ]
            
            # Fill remaining characters
            remaining_length = length - 4
            all_chars = lowercase + uppercase + digits + special_chars
            password.extend(random.choice(all_chars) for _ in range(remaining_length))
            
            # Shuffle password
            random.shuffle(password)
            password = ''.join(password)
            
            # Display password
            self.password_var.set(password)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()