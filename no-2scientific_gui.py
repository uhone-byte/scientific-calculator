import tkinter as tk
import math

# Function to update the display
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(display.get().replace('^', '**').replace('π', 'math.pi').replace('e', 'math.e')))
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif text == "C":
        display.set("")
    elif text == "sin":
        display.set(str(math.sin(math.radians(float(display.get())))))
    elif text == "cos":
        display.set(str(math.cos(math.radians(float(display.get())))))
    elif text == "tan":
        display.set(str(math.tan(math.radians(float(display.get())))))
    elif text == "log":
        display.set(str(math.log10(float(display.get()))))
    elif text == "ln":
        display.set(str(math.log(float(display.get()))))
    elif text == "sqrt":
        display.set(str(math.sqrt(float(display.get()))))
    elif text == "exp":
        display.set(str(math.exp(float(display.get()))))
    elif text == "fact":
        display.set(str(math.factorial(int(display.get()))))
    elif text == "nCr":
        values = display.get().split(',')
        if len(values) == 2:
            n, r = map(int, values)
            display.set(str(math.comb(n, r)))
    elif text == "nPr":
        values = display.get().split(',')
        if len(values) == 2:
            n, r = map(int, values)
            display.set(str(math.perm(n, r)))
    else:
        display.set(display.get() + text)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("300x500")  # Set the width and height of the window
root.configure(bg="#d4d4d2")  # Set the background color

# Create the display
display = tk.StringVar()
entry = tk.Entry(root, textvar=display, font=("Arial", 20), bg="white", fg="black", bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button configuration
buttons = [
    ["7", "8", "9", "/", "sin", "cos", "tan"],
    ["4", "5", "6", "*", "log", "ln", "sqrt"],
    ["1", "2", "3", "-", "(", ")", "^"],
    ["C", "0", "=", "+", "π", ".", "exp"],
    ["fact", "nCr", "nPr", "e"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#d4d4d2")
    frame.pack(expand=True, fill=tk.BOTH)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font=("Arial", 14), bg="#f1f2f3", fg="black", bd=1, relief=tk.RAISED)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
