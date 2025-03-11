
import tkinter as tk

# create main application window
root=tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x100")


def say_hello():
     print('Hello,World')
     print('Good Bye')
     
hello_button=tk.Button(root,text="Click Me",command=say_hello)    
hello_button.pack(pady=20) 
root.mainloop()