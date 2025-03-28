import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import hashlib
import re

class AuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',  # Replace with your MySQL password
            'database': 'user_auth_db'
        }
        
        # Create a connection to MySQL
        try:
            self.connection = self.create_db_connection()
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")
        
        # Create frames
        self.login_frame = tk.Frame(root)
        self.register_frame = tk.Frame(root)
        self.welcome_frame = tk.Frame(root)
        
        self.create_login_frame()
        self.create_register_frame()
        self.create_welcome_frame()
        
        # Show login frame initially
        self.show_login_frame()
    
    def create_db_connection(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            raise
    
    def create_login_frame(self):
        tk.Label(self.login_frame, text="Login", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.login_frame, text="Username:").pack(pady=5)
        self.login_username = tk.Entry(self.login_frame, width=30)
        self.login_username.pack(pady=5)
        
        tk.Label(self.login_frame, text="Password:").pack(pady=5)
        self.login_password = tk.Entry(self.login_frame, width=30, show="*")
        self.login_password.pack(pady=5)
        
        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.login_frame, text="Register", command=self.show_register_frame).pack()
    
    def create_register_frame(self):
        tk.Label(self.register_frame, text="Register", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.register_frame, text="Username:").pack(pady=5)
        self.register_username = tk.Entry(self.register_frame, width=30)
        self.register_username.pack(pady=5)
        
        tk.Label(self.register_frame, text="Email:").pack(pady=5)
        self.register_email = tk.Entry(self.register_frame, width=30)
        self.register_email.pack(pady=5)
        
        tk.Label(self.register_frame, text="Password:").pack(pady=5)
        self.register_password = tk.Entry(self.register_frame, width=30, show="*")
        self.register_password.pack(pady=5)
        
        tk.Button(self.register_frame, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.register_frame, text="Back to Login", command=self.show_login_frame).pack()
    
    def create_welcome_frame(self):
        tk.Label(self.welcome_frame, text="Welcome!", font=("Arial", 16)).pack(pady=10)
        self.welcome_label = tk.Label(self.welcome_frame, text="")
        self.welcome_label.pack(pady=10)
        tk.Button(self.welcome_frame, text="Logout", command=self.logout).pack(pady=10)
    
    def show_login_frame(self):
        self.register_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)
    
    def show_register_frame(self):
        self.login_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)
    
    def show_welcome_frame(self, username):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.welcome_label.config(text=f"Welcome, {username}!")
        self.welcome_frame.pack(fill="both", expand=True)
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        try:
            connection = self.create_db_connection()
            cursor = connection.cursor()
            
            # Check if user exists
            query = "SELECT password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            
            if result and result[0] == self.hash_password(password):
                self.show_welcome_frame(username)
            else:
                messagebox.showerror("Error", "Invalid username or password")
            
            cursor.close()
            connection.close()
        except Error as e:
            messagebox.showerror("Database Error", f"Error during login: {e}")
    
    def register(self):
        username = self.register_username.get()
        email = self.register_email.get()
        password = self.register_password.get()
        
        if not username or not email or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            return
        
        try:
            connection = self.create_db_connection()
            cursor = connection.cursor()
            
            # Check if username already exists
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                cursor.close()
                connection.close()
                return
            
            # Check if email already exists
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Email already registered")
                cursor.close()
                connection.close()
                return
            
            # Insert new user
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, self.hash_password(password)))
            connection.commit()
            
            messagebox.showinfo("Success", "Registration successful! You can now login.")
            self.show_login_frame()
            
            cursor.close()
            connection.close()
        except Error as e:
            messagebox.showerror("Database Error", f"Error during registration: {e}")
    
    def logout(self):
        self.login_username.delete(0, tk.END)
        self.login_password.delete(0, tk.END)
        self.show_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthenticationApp(root)
    root.mainloop()