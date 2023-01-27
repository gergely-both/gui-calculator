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
        self.label.grid(row=0, column=0, columnspan=2)
        self.button_back = tk.Button(master, text="BACK", command=lambda: self.parse_input("BACK"), **button_properties)
        self.button_back.grid(row=0, column=2)
        self.button_clear = tk.Button(master, text="C", command=lambda: self.parse_input("C"), **button_properties)
        self.button_clear.grid(row=0, column=3)
        self.button_allclear = tk.Button(master, text="AC", command=lambda: self.parse_input("AC"), **button_properties)
        self.button_allclear.grid(row=0, column=4)
        self.button_7 = tk.Button(master, text=7, command=lambda: self.parse_input(7), **button_properties)
        self.button_7.grid(row=1, column=0)
        self.button_8 = tk.Button(master, text=8, command=lambda: self.parse_input(8), **button_properties)
        self.button_8.grid(row=1, column=1)
        self.button_9 = tk.Button(master, text=9, command=lambda: self.parse_input(9), **button_properties)
        self.button_9.grid(row=1, column=2)
        self.button_mul = tk.Button(master, text="*", command=lambda: self.parse_input("*"), **button_properties)
        self.button_mul.grid(row=1, column=3)
        self.button_sign = tk.Button(master, text="SIG", command=lambda: self.parse_input("SIG"), **button_properties)
        self.button_sign.grid(row=1, column=4)
        self.button_4 = tk.Button(master, text=4, command=lambda: self.parse_input(4), **button_properties)
        self.button_4.grid(row=2, column=0)
        self.button_5 = tk.Button(master, text=5, command=lambda: self.parse_input(5), **button_properties)
        self.button_5.grid(row=2, column=1)
        self.button_6 = tk.Button(master, text=6, command=lambda: self.parse_input(6), **button_properties)
        self.button_6.grid(row=2, column=2)
        self.button_div = tk.Button(master, text="/", command=lambda: self.parse_input("/"), **button_properties)
        self.button_div.grid(row=2, column=3)
        self.button_memp = tk.Button(master, text="m+", command=lambda: self.parse_input("m+"), **button_properties)
        self.button_memp.grid(row=2, column=4)
        self.button_1 = tk.Button(master, text=1, command=lambda: self.parse_input(1), **button_properties)
        self.button_1.grid(row=3, column=0)
        self.button_2 = tk.Button(master, text=2, command=lambda: self.parse_input(2), **button_properties)
        self.button_2.grid(row=3, column=1)
        self.button_3 = tk.Button(master, text=3, command=lambda: self.parse_input(3), **button_properties)
        self.button_3.grid(row=3, column=2)
        self.button_sub = tk.Button(master, text="-", command=lambda: self.parse_input("-"), **button_properties)
        self.button_sub.grid(row=3, column=3)
        self.button_memm = tk.Button(master, text="m-", command=lambda: self.parse_input("m-"), **button_properties)
        self.button_memm.grid(row=3, column=4)
        self.button_dec = tk.Button(master, text=".", command=lambda: self.parse_input("."), **button_properties)
        self.button_dec.grid(row=4, column=0)
        self.button_0 = tk.Button(master, text=0, command=lambda: self.parse_input(0), **button_properties)
        self.button_0.grid(row=4, column=1)
        self.button_eq = tk.Button(master, text="=", command=lambda: self.parse_input("="), **button_properties)
        self.button_eq.grid(row=4, column=2)
        self.button_add = tk.Button(master, text="+", command=lambda: self.parse_input("+"), **button_properties)
        self.button_add.grid(row=4, column=3)
        self.button_memr = tk.Button(master, text="mr", command=lambda: self.parse_input("mr"), **button_properties)
        self.button_memr.grid(row=4, column=4)

        self.opset = {"+", "-", "*", "/", "="}
        self.numeric_input = []
        self.query = []
        self.memory = "0"

    def display_input(self):
        self.label.config(text="".join(self.numeric_input))

    def dotted_value(self):
        if not self.numeric_input:
            self.numeric_input.extend(["0", "."]) 
            self.display_input()
        elif "." not in self.numeric_input:
            self.numeric_input.append(".")
            self.display_input()

    def change_sign(self):
        sign = "-"
        if self.numeric_input and (len(self.numeric_input) > 1 or self.numeric_input[0] != "0"):
            if self.numeric_input[0] == sign:
                del self.numeric_input[0]
            else:
                self.numeric_input.insert(0, sign)    
            self.display_input()
        elif len(self.query) == 1 and "0" not in self.query:
            if sign in self.query[0]:
                self.query[0] = self.query[0][1:]
            else:
                self.query[0] = sign + self.query[0]
            self.label.config(text=self.query[0])

    def clear_input(self):
        self.numeric_input.clear()
        self.label.config(text=0)

    # def clear_all(self):
    #     self.numeric_input.clear()
    #     self.query.clear()
    #     self.label.config(text=0)

    def remove_last(self):
        if self.numeric_input:
            self.numeric_input.pop()
            self.label.config(text="".join(self.numeric_input) or 0)

    def memory_operate(self, value):
        operation = value[1]
        self.memory = str(eval(self.memory + operation + ("".join(self.numeric_input) or self.query[0])))
        self.numeric_input.clear()
  
    def memory_recall(self):
        self.numeric_input = [i for i in self.memory]
        self.display_input()

    def input_operator(self, operator):
        previous_value = "".join(self.numeric_input)
        self.numeric_input.clear()
        if not self.query:
            if operator == "=":
                self.query.append(previous_value if previous_value else "0")
            else:
                self.query.extend([previous_value if previous_value else "0", operator])
        elif len(self.query) == 1:
            if operator == "=":
                self.query[0] = previous_value if previous_value else self.query[0]
            else:
                self.query.append(operator)
        elif len(self.query) == 2:
            if previous_value:
                self.query.append(previous_value)
                self.equals_to(operator)
            elif operator == "=" and not previous_value:
                self.query.append(self.query[0])
                self.equals_to(operator)
            elif operator != "=" and not previous_value:
                self.query[-1] = operator

    def equals_to(self, operator):
        unrounded = eval("".join(self.query))
        total = round(unrounded, 10)
        total = int(total) if int(total) == total else total
        self.query.clear()
        if operator == "=":
            self.query.append(str(total))
        else:
            self.query.extend([str(total), operator])
        self.label.config(text=total)

    def input_digit(self, value):
        if self.numeric_input:
            if len(self.numeric_input) == 1 and self.numeric_input[0] == "0":
                if value != "0":
                    self.numeric_input[0] = str(value)
                    self.label.config(text=self.numeric_input[0])
            else:
                self.numeric_input.append(str(value))
                self.display_input()
        else:
            self.numeric_input.append(str(value))
            self.label.config(text=self.numeric_input[0])

    def input_symbol(self, value):
        if value in self.opset:
            self.input_operator(value)
        elif value == ".":
            self.dotted_value()
        elif value == "SIG":
            self.change_sign()
        elif value == "BACK":
            self.remove_last()
        elif value == "C":
            self.clear_input()
        elif value == "AC":
            self.clear_input()
            self.query.clear()
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
