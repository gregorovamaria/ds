import os
import subprocess  # To open folder on Windows


# Function to close the main window
def close_window(root):
    root.destroy()


# Function to update status about the search function
def update_status(status_label, message, color):
    status_label.config(text=message, foreground=color, width=100, anchor="center")


# Function to open the folder containing the file
def open_folder(file_path):

    folder = os.path.dirname(file_path)  # Get the folder path
    folder_path = f"{folder}/SearchResults"

    if os.name == "nt":  # If it's a Windows system
        os.startfile(folder_path, "open")
    elif os.name == "posix":  # For Linux/macOS
        subprocess.run(["xdg-open", folder_path])  # Use xdg-open to open the folder


# Function to create folder
def create_folder(file_path):
    folder = os.path.dirname(file_path)

    folder_path = f"{folder}/SearchResults"
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


# Function to create a clickable link (Label) to open the folder containing the file
# ROW 5
def open_folder_label_fn(label, main, file_path, text):
    open_folder_label = label(
        main,
        text=text,
        font=("Calibri", 12, "bold"),
        foreground="blue",
        cursor="hand2",  # Change cursor to hand when hovering over the link
        width=100,
        anchor="center",
    )
    open_folder_label.grid(column=0, row=5, columnspan=3, pady=10)

    # Bind the label to the open_folder function
    open_folder_label.bind("<Button-1>", lambda event: open_folder(file_path))
