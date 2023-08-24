import tkinter as tk
from tkinter import messagebox
import os


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        completed_listbox.insert(tk.END, task)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                listbox.insert(tk.END, task)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


root = tk.Tk()
root.title("TO-DO LIST")


listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)
listbox.configure(bg="#f1f28a")



entry = tk.Entry(root)
entry.pack(pady=5)
entry.configure(bg="#f1f28a")



add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.configure(bg="#d45af2")
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.configure(bg="#d45af2")
completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
completed_button.configure(bg="#d45af2")

add_button.pack(padx=10, pady=5)
remove_button.pack(padx=10, pady=5)
completed_button.pack(padx=10, pady=5)


completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
completed_listbox.pack(pady=10)
completed_listbox.configure(bg="#f1f28a")



load_tasks()


menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Tasks", command=save_tasks)
root.configure(bg="#535154")


root.mainloop()
