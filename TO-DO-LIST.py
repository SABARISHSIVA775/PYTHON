import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, f"{len(task_listbox.get(0, tk.END)) + 1}. {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_as_completed():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.itemconfig(index, {'bg':'light grey'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")
root.configure(bg='lightblue')

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

task_listbox = tk.Listbox(root, width=50)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.grid(row=2, column=0, padx=5, pady=10)

completed_button = tk.Button(root, text="Mark as Completed", width=15, command=mark_as_completed)
completed_button.grid(row=2, column=1, padx=5, pady=10)

root.mainloop()
