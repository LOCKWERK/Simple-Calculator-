import tkinter as tk
from tkinter import messagebox

def on_click (operation):
  try:
    num1= float(entry_num1.get())#gets the value of the entry widget num1
    num2 = float(entry_num2.get())#gets the value of the entry widget num2
    if operation == "add": #this field is for addition
      result = num1 + num2
    elif operation == "subtract":#this field is for subtraction
      result = num1 - num2
    elif operation == "multiply":#this field is for multiplication
      result = num1 * num2
    elif operation == "divide":#this field is for division
      if num2 == 0 :
        messagebox.showerror("error", "division by zero is not allowed.")
        label_result.config(text = "Result: Error")#show error if zero is entered
        return
      result = num1 / num2
    else:
      messagebox.showerror("error", "Invalid operation.")
      return
    if result.is_integer():
      result = int(result)
    label_result.config(text = f"Result: {result}")
  except ValueError:
      messagebox.showerror("input error", "Please enter valid numbers")
      label_result.config(text = "Result: Error")
      
root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")

font_large = ("Arial", 16)
font_result = ("Arial", 20, "bold")

label_num1 = tk.Label(root, text="Enter the first number:", font=font_large)
label_num1.pack(pady=10)

entry_num1 = tk.Entry(root, font=font_large, width=10)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter the second number:", font=font_large)
label_num2.pack(pady=10)

entry_num2 = tk.Entry(root, font=font_large, width=10)
entry_num2.pack(pady=5)

button_add = tk.Button(root, text="Add", command=lambda: on_click('add'), font=font_large, width=10)
button_add.pack(pady=5)

button_subtract = tk.Button(root, text="Subtract", command=lambda: on_click("subtract"), font=font_large, width=10)
button_subtract.pack(pady=5)

button_multiply = tk.Button(root, text="Multiply", command=lambda: on_click("multiply"), font=font_large, width=10)
button_multiply.pack(pady=5)

button_divide = tk.Button(root, text="Divide", command=lambda: on_click("divide"), font=font_large, width=10)
button_divide.pack(pady=5)

label_result = tk.Label(root, text="Result:", font=font_result)
label_result.pack(pady=20)

root.mainloop()