import tkinter as tk

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)


# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right"
)

display.pack(
    padx=10,
    pady=20,
    fill="x"
)


# Function to add numbers/operators
def click(value):
    display.insert(tk.END, value)


# Clear display
def clear():
    display.delete(0, tk.END)


# Calculate result
def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]


# Create button frame
frame = tk.Frame(root)
frame.pack()


row = 0
col = 0


for button in buttons:

    if button == "C":
        command = clear

    elif button == "=":
        command = calculate

    else:
        command = lambda x=button: click(x)

    tk.Button(
        frame,
        text=button,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    ).grid(
        row=row,
        column=col,
        padx=5,
        pady=5
    )

    col += 1

    if col == 4:
        col = 0
        row += 1


# Start calculator
root.mainloop()