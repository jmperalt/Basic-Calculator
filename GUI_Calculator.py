import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget for input/output
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create buttons for digits
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)

        # create buttons for operators
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        # create buttons for other functions
        self.create_button("C", 4, 0)
        self.create_button(".", 4, 2)
        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1, rowspan=1):
        # create a button and set its command to button_click
        button = tk.Button(self.master, text=text, padx=40, pady=20,
                           command=lambda: self.button_click(text))
        # position the button
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

    def button_click(self, text):
        # get the current text in the entry widget
        current = self.entry.get()

        if text == "C":
            # clear the entry widget if "C" is clicked
            self.entry.delete(0, tk.END)
        elif text == "=":
            try:
                # evaluate the expression and display the result
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                # display an error message if evaluation fails
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            # append the clicked button's text to the entry widget
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(current) + str(text))


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
