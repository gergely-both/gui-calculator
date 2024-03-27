import tkinter as tk
import math


button_properties = {
    "width": 9,
    "relief": "raised"
}


class Calculator:
    """Python calculator with basic arithmetic operations and memory functions."""
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
        self.button_sqrt = tk.Button(master, text="√", command=lambda: self.parse_input("√"), **button_properties)
        self.button_sqrt.grid(row=5, column=4)
        self.button_squared = tk.Button(master, text="^2", command=lambda: self.parse_input("^2"), **button_properties)
        self.button_squared.grid(row=5, column=3)
        self.button_PI = tk.Button(master, text="π", command=lambda: self.parse_input("π"), **button_properties)
        self.button_PI.grid(row=5, column=2)
        
        self.opset = {"+", "-", "*", "/", "="} # mathematical operators collection
        self.numeric_input = [] # numeric user input for query making
        self.query = [] # query for calculation containing numbers and operators
        self.memory = "0" # zero initial value for memory
        self.history = [] # calculator memory to repeat last calculation

    def parse_input(self, value):
        """input dispatcher for numeric, operator, or function value types"""
        if type(value) == int:
            self.input_number(value)
        elif type(value) == str:
            if value == "π":
                self.input_number(math.pi)
            else:
                self.input_symbol(value)

    def input_number(self, value):
        """appends to empty list; replaces leading zero or appends further"""
        if self.numeric_input:
            if self.numeric_input[0] == "0" and value != "0":
                self.numeric_input[0] = str(value)
                self.label.config(text=self.numeric_input[0])
            else:
                self.numeric_input.append(str(value))
                self.display_input()
        else:
            self.numeric_input.append(str(value))
            self.label.config(text=self.numeric_input[0])

    def input_symbol(self, value):
        """dispatches by mathematical operator or other function"""
        if value in self.opset:
            self.input_operator(value)
        elif value == ".":
            self.dot_value()
        elif value == "SIG":
            self.swap_sign()
        elif value == "BACK":
            self.remove_last()
        elif value == "C":
            self.clear_user_input()
        elif value == "AC":
            self.clear_user_input()
            self.query.clear()
        elif value in {"m+", "m-"}:
            self.memory_operate(value)
        elif value == "mr":
            self.memory_recall()
        elif value == "√":
            self.make_sqrt()
        elif value == "^2":
            self.make_squared()

    def input_operator(self, operator):
        """number|operator|number stage finder; reads input, appends further or calculates"""
        previous_value = "".join(self.numeric_input)
        self.numeric_input.clear()
        
        if not self.query:
            self.query.append(previous_value if previous_value else "0")
            if operator != "=":
                self.query.append(operator)

        elif len(self.query) == 1:
            if operator == "=" and previous_value:
                self.query[0] = previous_value
            elif operator == "=" and not previous_value and self.history:
                self.query.extend(self.history[1:])
                self.calculate(operator)
            elif operator != "=":
                if previous_value:
                    self.query[0] = previous_value
                self.query.append(operator)

        elif len(self.query) == 2:
            if not previous_value:
                if operator == "=":
                    del self.query[1]
                else:
                    self.query[-1] = operator
            else:
                self.query.append(previous_value)
                self.calculate(operator)

    def calculate(self, operator):
        """evaluates query, rounds result, updates query, and label text"""
        self.history.clear()
        self.history.extend(self.query)
        unrounded = eval("".join(self.query))
        total_raw = round(unrounded, 10)
        total = int(total_raw) if int(total_raw) == total_raw else total_raw
        self.query.clear()
        if operator == "=":
            self.query.append(str(total))
        else:
            self.query.extend([str(total), operator])
        self.label.config(text=total)

    def clear_user_input(self):
        """clears current numeric input and label text"""
        self.numeric_input.clear()
        self.label.config(text=0)

    def remove_last(self):
        """removes last character from numeric input and updates label text"""
        if self.numeric_input:
            self.numeric_input.pop()
            self.label.config(text="".join(self.numeric_input) or "0")
        
    def display_input(self):
        """displays current numeric input on label"""
        self.label.config(text="".join(self.numeric_input))

    def dot_value(self):
        """appends dot to numeric input if not present"""
        if not self.numeric_input:
            self.numeric_input.extend(["0", "."]) 
            self.display_input()
        elif "." not in self.numeric_input:
            self.numeric_input.append(".")
            self.display_input()

    def swap_sign(self):
        """swaps sign of numeric input or query"""
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

    def memory_operate(self, value):
        """adds or subtracts current numeric input or query from memory"""
        operation = "+" if value[1] == "+" else "-"
        self.memory = str(eval(self.memory + operation + ("".join(self.numeric_input) or self.query[0])))
        self.numeric_input.clear()
  
    def memory_recall(self):
        """recalls memory value to query or numeric input"""
        self.numeric_input = [char for char in self.memory]
        self.display_input()
            
    def make_sqrt(self):
        """calculates square root of numeric input or query and updates label text"""
        if self.numeric_input:
            sqrt_result = math.sqrt(float("".join(self.numeric_input)))
            sqrt_pruned = int(sqrt_result) if int(sqrt_result) == sqrt_result else sqrt_result
            self.query.append(str(sqrt_pruned))
            self.numeric_input.clear()
        elif not self.numeric_input and len(self.query)==1:
            sqrt_result = math.sqrt(float(self.query[0]))
            sqrt_pruned = int(sqrt_result) if int(sqrt_result) == sqrt_result else sqrt_result
            self.query[0] = str(sqrt_pruned)
        elif not self.numeric_input and len(self.query)==2:
            sqrt_result = math.sqrt(float(self.query[0]))
            sqrt_pruned = int(sqrt_result) if int(sqrt_result) == sqrt_result else sqrt_result
            self.query[0] = str(sqrt_pruned)
        self.label.config(text=sqrt_pruned)

    def make_squared(self):
        """calculates square of numeric input or query and updates label text"""
        if self.numeric_input:
            squared_result = float("".join(self.numeric_input)) ** 2
            squared_pruned = int(squared_result) if int(squared_result) == squared_result else squared_result
            self.query.append(str(squared_pruned))
            self.numeric_input.clear()
        elif not self.numeric_input and len(self.query)==1:
            squared_result = float(self.query[0]) ** 2
            squared_pruned = int(squared_result) if int(squared_result) == squared_result else squared_result
            self.query[0] = str(squared_pruned)
        elif not self.numeric_input and len(self.query)==2:
            squared_result = float(self.query[0]) ** 2
            squared_pruned = int(squared_result) if int(squared_result) == squared_result else squared_result
            self.query[0] = str(squared_pruned)
        self.label.config(text=squared_pruned)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
