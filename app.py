import tkinter as tk
from tkinter import ttk
from tkinter import font

class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x500")
        self.master.resizable(True, True)
        self.master.title("To-Do List")

        # Set system look and feel
        style = ttk.Style()
        style.theme_use("aqua")
        
        # Create the title label
        title_label = tk.Label(self.master, text="Rio's Badass ToDo List", font=("Arial", 24) )
        title_label.pack(side=tk.TOP, pady=10)

        # Create a frame to hold the task input and add button
        input_frame = tk.Frame(self.master, background="white")
        input_frame.pack(fill=tk.X, padx=20, pady=20)

        # Create task input
        self.task_input = tk.Entry(input_frame, font=("Arial", 14))
        self.task_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.task_input.focus_set()

        # Create add button
        add_button = tk.Button(input_frame, text="Add", font=("Arial", 14), command=self.add_task)
        add_button.pack(side=tk.RIGHT)

        # Create a listbox to hold tasks
        self.task_listbox = tk.Listbox(
            self.master, font=("Arial", 16), selectmode=tk.SINGLE, background=style.lookup("TFrame", "background"),
            foreground="#C7C7CC", borderwidth=0, highlightthickness=0, selectbackground="#5b5b5b",  border=0, selectborderwidth=0, activestyle="none"
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create a delete button
        delete_button = tk.Button(self.master, text="Delete", font=("Arial", 14), command=self.delete_task)
        delete_button.pack(side=tk.BOTTOM, pady=10)

        # Bind the "Return" key to add a task
        self.task_input.bind("<Return>", self.add_task)
       
        # Bind the "Delete" key to delete a task
        self.task_listbox.bind("<Delete>", self.delete_task)
        self.task_listbox.bind("<BackSpace>", self.delete_task)
        
        # Bind double-click on a task to toggle its completion status
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task_complete)
        
        # Dictionary to store the completion status of each task
        self.task_complete = {}

    def add_task(self, event=None):
        task = self.task_input.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)

    def delete_task(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
            
    def toggle_task_complete(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            if task in self.task_complete:
                self.task_complete[task] = not self.task_complete[task]
            else:
                self.task_complete[task] = True
            if self.task_complete[task]:
                self.task_listbox.itemconfig(selected, foreground="#C7C7CC")
            else:
                self.task_listbox.itemconfig(selected, foreground="#000000")

print("Starting app...")
window = tk.Tk()
app = TodoList(window)
window.mainloop()
