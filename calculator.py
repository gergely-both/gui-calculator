import tkinter as tk


button_properties = {
    "width": 9,
    "relief": "raised"
}

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Python calculator")
        self.label = tk.Label(master, text=0)
        self.label.grid(row=0, column=0, columnspan=3)
        self.button_back = tk.Button(master, text="BACK", command=lambda: self.parse_input("BACK"), **button_properties)
        self.button_back.grid(row=0, column=3)
        self.button_7 = tk.Button(master, text=7, command=lambda: self.parse_input(7), **button_properties)
        self.button_7.grid(row=1, column=0)
        self.button_8 = tk.Button(master, text=8, command=lambda: self.parse_input(8), **button_properties)
        self.button_8.grid(row=1, column=1)
        self.button_9 = tk.Button(master, text=9, command=lambda: self.parse_input(9), **button_properties)
        self.button_9.grid(row=1, column=2)
        self.button_plus = tk.Button(master, text="*", command=lambda: self.parse_input("*"), **button_properties)
        self.button_plus.grid(row=1, column=3)
        self.button_4 = tk.Button(master, text=4, command=lambda: self.parse_input(4), **button_properties)
        self.button_4.grid(row=2, column=0)
        self.button_5 = tk.Button(master, text=5, command=lambda: self.parse_input(5), **button_properties)
        self.button_5.grid(row=2, column=1)
        self.button_6 = tk.Button(master, text=6, command=lambda: self.parse_input(6), **button_properties)
        self.button_6.grid(row=2, column=2)
        self.button_minus = tk.Button(master, text="/", command=lambda: self.parse_input("/"), **button_properties)
        self.button_minus.grid(row=2, column=3)
        self.button_1 = tk.Button(master, text=1, command=lambda: self.parse_input(1), **button_properties)
        self.button_1.grid(row=3, column=0)
        self.button_2 = tk.Button(master, text=2, command=lambda: self.parse_input(2), **button_properties)
        self.button_2.grid(row=3, column=1)
        self.button_3 = tk.Button(master, text=3, command=lambda: self.parse_input(3), **button_properties)
        self.button_3.grid(row=3, column=2)
        self.button_times = tk.Button(master, text="-", command=lambda: self.parse_input("-"), **button_properties)
        self.button_times.grid(row=3, column=3)
        self.button_dot = tk.Button(master, text=".", command=lambda: self.parse_input("."), **button_properties)
        self.button_dot.grid(row=4, column=0)
        self.button_0 = tk.Button(master, text=0, command=lambda: self.parse_input(0), **button_properties)
        self.button_0.grid(row=4, column=1)
        self.button_equals = tk.Button(master, text="=", command=lambda: self.parse_input("="), **button_properties)
        self.button_equals.grid(row=4, column=2)
        self.button_div = tk.Button(master, text="+", command=lambda: self.parse_input("+"), **button_properties)
        self.button_div.grid(row=4, column=3)
        self.button_div = tk.Button(master, text="C", command=lambda: self.parse_input("C"), **button_properties)
        self.button_div.grid(row=0, column=4)
        self.button_div = tk.Button(master, text="SIG", command=lambda: self.parse_input("SIG"), **button_properties)
        self.button_div.grid(row=1, column=4)
        self.button_div = tk.Button(master, text="m+", command=lambda: self.parse_input("m+"), **button_properties)
        self.button_div.grid(row=2, column=4)
        self.button_div = tk.Button(master, text="m-", command=lambda: self.parse_input("m-"), **button_properties)
        self.button_div.grid(row=3, column=4)
        self.button_div = tk.Button(master, text="mr", command=lambda: self.parse_input("mr"), **button_properties)
        self.button_div.grid(row=4, column=4)


        self.user_input = []
        self.query = []
        self.memory = "0"


    def display_input(self):
        self.label.config(text="".join(self.user_input))

    def dotted_value(self):
        if not self.user_input:
            self.user_input.extend(["0", "."]) 
            self.display_input()
        elif "." not in self.user_input:
            self.user_input.append(".")
            self.display_input()

    def change_sign(self):
        sign = "-"
        if self.user_input and (len(self.user_input) != 1 or self.user_input[0] != "0"):
            if self.user_input[0] == sign:
                del self.user_input[0]
            else:
                self.user_input.insert(0, sign)    
            self.display_input()
        elif len(self.query) == 1 and "0" not in self.query:
            if sign in self.query[0]:
                self.query[0] = self.query[0][1:]
            else:
                self.query[0] = sign + self.query[0]
            self.label.config(text=self.query[0])

    def clear_input(self):
        self.user_input.clear()
        self.label.config(text=0)

    def remove_last(self):
        if self.user_input:
            self.user_input.pop()
            self.label.config(text="".join(self.user_input) or 0)

    def memory_operate(self, value):
        operation = value[1]
        self.memory = str(eval(self.memory + operation + ("".join(self.user_input) or self.query[0])))
        self.user_input.clear()
  
    def memory_recall(self):
        self.user_input = [i for i in self.memory]
        self.display_input()

    def input_operator(self, value):
        number = "".join(self.user_input) or "0"
        self.user_input.clear()
        if not self.query:
            if value == "=":
                self.query.append(number)
            else:
                self.query.extend([number, value])
        elif len(self.query) == 1:
            if number and number != "0":
                if value == "=":
                    self.query.clear()
                    self.query.append(number)
                else:
                    self.query.clear()
                    self.query.extend([number, value])
            else:
                if value == "=":
                    pass
                else:
                    self.query.append(value)
        elif len(self.query) > 1:
            if number and number != "0":
                if value == "=":
                    self.query.extend([number, value])
                    self.equals_to(value)
                else:
                    self.query.extend([number, value])
                    self.equals_to(value)
            else:
                if value == "=":
                    self.query.pop()
                else:
                    self.query[1] = value

    def equals_to(self, value):
        self.query.pop()
        total = eval("".join(self.query))
        self.query.clear()
        if value == "=":
            self.query.append(str(total))
        else:
            self.query.extend([str(total), value])
        self.label.config(text=total)

    def input_digit(self, value):
        if self.user_input:
            if len(self.user_input) == 1 and self.user_input[0] == "0":
                if value != "0":
                    self.user_input[0] = str(value)
                    self.label.config(text=self.user_input[0])
            else:
                self.user_input.append(str(value))
                self.display_input()
        else:
            self.user_input.append(str(value))
            self.label.config(text=self.user_input[0])

    def input_symbol(self, value):
        if value in {"+", "-", "*", "/", "="}:
            self.input_operator(value)
        elif value == ".":
            self.dotted_value()
        elif value == "SIG":
            self.change_sign()
        elif value == "BACK":
            self.remove_last()
        elif value == "C":
            self.clear_input()
        elif value in {"m+", "m-"}:
            self.memory_operate(value)
        elif value == "mr":
            self.memory_recall()

    def parse_input(self, value):
        if type(value) == int:
            self.input_digit(value)
        elif type(value) == str:
            self.input_symbol(value)

        
root = tk.Tk()
app = Calculator(root)
root.mainloop()
