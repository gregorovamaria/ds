import os, subprocess
from tkinter import ttk


# Function to create a clickable link to open the folder with search results
def _create_open_results_section(parent):
    open_results_label = ttk.Label(parent, text="", width=100, anchor="center")
    open_results_label.grid(column=0, row=5, columnspan=3, pady=30)
    return open_results_label


# Function to update a clickable link to open the folder with search results
def _update_open_results_section(open_results_label, message, target_folder):
    open_results_label.config(
        text=message,
        foreground="blue",
        cursor="hand2",
    )

    # Bind the label to the open_folder function
    open_results_label.bind("<Button-1>", lambda event: open_folder(target_folder))


# Function to open the folder containing the file
def open_folder(target_folder):
    # If it's a Windows system
    if os.name == "nt":
        os.startfile(target_folder, "open")
    # For Linux/macOS
    elif os.name == "posix":
        subprocess.run(["xdg-open", target_folder])  # Use xdg-open to open the folder
