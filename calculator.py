import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate mathematical expressions using the Shunting Yard algorithm
def evaluate_expression(expression):
    def tokenize(expr):
        tokens = []
        current = ""
        unary_pending = True
        for ch in expr:
            if ch.isdigit() or ch == ".":
                current += ch
                unary_pending = False
            elif ch in "+-*/^(){}":
                if current:
                    tokens.append(current)
                    current = ""
                if ch == "-" and unary_pending:  # Unary minus
                    tokens.append("u-")
                else:
                    tokens.append(ch)
                unary_pending = ch in "(+{-"  # Reset for next token
            elif ch.isalpha():
                current += ch
                unary_pending = False
            elif not ch.isspace():
                raise ValueError(f"Invalid character: {ch}")
        if current:
            tokens.append(current)
        return tokens

    def shunting_yard(tokens):
        output = []
        operators = []
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "u-": 4}
        associativity = {"+": "L", "-": "L", "*": "L", "/": "L", "^": "R"}

        functions = {"sin", "cos", "tan", "ln", "log10"}

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output.append(token)
            elif token in precedence:
                while (operators and operators[-1] in precedence and
                       ((associativity.get(token, "L") == "L" and precedence[token] <= precedence[operators[-1]]) or
                        (associativity.get(token, "R") == "R" and precedence[token] < precedence[operators[-1]]))):
                    output.append(operators.pop())
                operators.append(token)
            elif token in functions:
                operators.append(token)
            elif token == "u-":
                operators.append(token)
            elif token in "({":
                operators.append(token)
            elif token in ")}":
                while operators and operators[-1] not in "({":
                    output.append(operators.pop())
                if operators and operators[-1] in "({":
                    operators.pop()
            else:
                raise ValueError(f"Unexpected token: {token}")

        while operators:
            output.append(operators.pop())

        return output

    def evaluate_rpn(rpn):
        stack = []
        functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "ln": lambda x: math.log(x) if x > 0 else ValueError("ln: Non-positive argument"),
            "log10": lambda x: math.log10(x) if x > 0 else ValueError("log10: Non-positive argument")
        }
        for token in rpn:
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))
            elif token in functions:
                arg = stack.pop()
                if arg <= 0 and token in {"ln", "log10"}:
                    raise ValueError(f"{token}: Non-positive argument")
                stack.append(functions[token](arg))
            elif token == "u-":
                stack.append(-stack.pop())
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "/":
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)
                elif token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "^":
                    stack.append(a ** b)
        return stack[0]

    tokens = tokenize(expression)
    rpn = shunting_yard(tokens)
    return evaluate_rpn(rpn)

# Main GUI application
def create_calculator():
    def on_button_click(symbol):
        if symbol == "=":
            try:
                expression = entry.get()
                validate_expression(expression)
                result = evaluate_expression(expression)
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif symbol == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, symbol)

    def validate_expression(expression):
        allowed_chars = "0123456789.+-*/^(){} sincostanlnlog10"
        stack = []
        for ch in expression:
            if ch not in allowed_chars and not ch.isspace():
                raise ValueError(f"Invalid character in expression: {ch}")
            if ch in "({":
                stack.append(ch)
            elif ch in ")}":
                if not stack or (ch == ")" and stack[-1] != "(") or (ch == "}" and stack[-1] != "{"):
                    raise ValueError("Mismatched parentheses or brackets")
                stack.pop()
        if stack:
            raise ValueError("Mismatched parentheses or brackets")

    # Create main window
    root = tk.Tk()
    root.title("Python Calculator")
    root.geometry("400x600")

    # Entry widget for expression input/output
    entry = tk.Entry(root, font=("Arial", 20), justify="right")
    entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

    # Button layout
    buttons = [
        "sin", "cos", "tan", "cot", "C",  # Row 1 (5 columns)
        "ln", "log10", " ", "+",          # Row 2 (4 columns, 3rd position empty)
        "7", "8", "9", "/",               # Row 3 (4 columns)
        "4", "5", "6", "*",               # Row 4 (4 columns)
        "1", "2", "3", "-",               # Row 5 (4 columns)
        "0", ".", " ", "^",               # Row 6 (4 columns)
        "(", ")", "{", "}", "="           # Row 7 (5 columns)
    ]

    # Placement rules
    row_structure = [5, 4, 4, 4, 4, 4, 5]
    current_row = 1
    current_column = 0

    # Place buttons in the grid
    for btn_text in buttons:
        if current_column >= row_structure[current_row - 1]:  # Check column limit for the current row
            current_row += 1
            current_column = 0

        if btn_text != " ":  # Skip empty buttons
            btn = tk.Button(root, text=btn_text, font=("Arial", 18), command=lambda symbol=btn_text: on_button_click(symbol))
            btn.grid(row=current_row, column=current_column, sticky="nsew", padx=5, pady=5)
        current_column += 1

    # Configure grid weights
    for i in range(8):  # 7 rows + 1 for entry
        root.grid_rowconfigure(i, weight=1)
    for i in range(5):  # Maximum 5 columns
        root.grid_columnconfigure(i, weight=1)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_calculator()
