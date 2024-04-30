import tkinter as tk
from tkinter import messagebox

# Function to add an item to the to-do list
def add_item():
    item = entry.get()
    if item:
        todo_list.insert(tk.END, item)
        checkbox_state.append(tk.BooleanVar(value=False))
        checkbox = tk.Checkbutton(todo_list, variable=checkbox_state[-1])
        todo_list.window_create(tk.END, window=checkbox)
        todo_list.insert(tk.END, '\n')  # Add a newline after each checkbox
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item!")

# Function to remove an item from the to-do list
def remove_item():
    try:
        index = todo_list.curselection()[0]
        todo_list.delete(index, index+1)  # Delete both item and checkbox
        del checkbox_state[index]
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to remove!")

# Function to display the to-do list
def display_list():
    items = [todo_list.get(i) for i in range(todo_list.size()) if i % 2 == 0]  # Skip the checkboxes
    if items:
        message = "\n".join(items)
        messagebox.showinfo("To-Do List", message)
    else:
        messagebox.showinfo("To-Do List", "The to-do list is empty!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Allow horizontal and vertical resizing
root.resizable(True, True)

# Create the label for the entry widget
label = tk.Label(root, text="Add new item:")
label.grid(row=0, column=0, padx=(5, 0), pady=5)  # Adjust the padx to set left padding only

# Create the entry widget to input items
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="ew")  # Adjust the padx to set right padding only

# Create the add button
add_button = tk.Button(root, text="Add", command=add_item)
add_button.grid(row=0, column=2, padx=5, pady=5)

# Create the remove button
remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.grid(row=1, column=0, padx=5, pady=5)

# Create the display button
display_button = tk.Button(root, text="Display", command=display_list)
display_button.grid(row=1, column=1, padx=5, pady=5)

# Create the to-do list
todo_list = tk.Listbox(root, width=50)
todo_list.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Configure resizing behavior
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# List to hold checkbox states
checkbox_state = []

root.mainloop()
