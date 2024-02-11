import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a positive integer.")
        else:
            generated_password = generate_password(length)
            generated_password_entry.config(state="normal")
            generated_password_entry.delete(0, tk.END)
            generated_password_entry.insert(0, generated_password)
            generated_password_entry.config(state="readonly")
            result_label.config(text="")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

def reset_button_clicked():
    length_entry.delete(0, tk.END)
    generated_password_entry.config(state="normal")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.config(state="readonly")
    result_label.config(text="")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")  

style = ThemedStyle(root)
style.set_theme("plastik")  

style.configure('.', background='#FFFFFF', foreground='#000000')  
style.configure('TLabel', font=('Arial', 12), foreground='#000000') 
style.configure('TButton', font=('Arial', 12))  

length_label = ttk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack(pady=10)

generated_password_entry = ttk.Entry(root, state="readonly")
generated_password_entry.pack(pady=10)

reset_button = ttk.Button(root, text="Reset", command=reset_button_clicked)
reset_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
