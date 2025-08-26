# import tkinter for buidling the UI
import tkinter as tk
from tkinter import messagebox

# functions for operations 
# addition 
def add(a, b):
    return a+b

# subtraction 
def subtract(a, b ):
    return a-b

# multiply 
def multiply(a, b ):
    return a*b

# divide 
def divide(a, b ):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a/b


# Function to perform calculation 

def calculate ():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()




        if operation == "Add":
            result  = add( num1, num2)

        elif operation == "Subtract":
            result = subtract(num1, num2)
        
        elif operation == "Multiply":
            result = multiply(num1, num2)

        elif operation == "Divide":
            result = divide(num1, num2)

        else:
            result = "select an operation"

# format of result presentation 
        label_result.config(text = f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Invalid input!")



# Main window 
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.config(bg="#f2f2f2")


# Input fields
tk.Label(root, text="Enter first number:", bg="#f2f2f2").pack(pady=5)
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#f2f2f2").pack(pady=5)
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack(pady=5)

# Operation dropdown
operation_var = tk.StringVar(value="Select Operation")
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.OptionMenu(root, operation_var, *operations).pack(pady=10)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), bg="#f2f2f2")
label_result.pack(pady=10)

# Run the application
root.mainloop()