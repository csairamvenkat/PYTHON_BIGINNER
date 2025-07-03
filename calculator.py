import tkinter as tk

def on_click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Set up the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget for the display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place the buttons on the grid
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=4, height=2, font=('Arial', 18),
                       command=lambda key=button_text: on_click(key))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
root.mainloop()
