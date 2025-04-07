from tkinter import ttk


# Function to create status about the search function
def _create_status_label(parent):
    status_label = ttk.Label(parent, text="")
    status_label.grid(column=0, row=4, columnspan=3, pady=25, ipady=5)
    return status_label


# Function to update status about the search function
def _update_status_label(status_label, message, color):
    status_label.config(text=message, foreground=color, width=100, anchor="center")
