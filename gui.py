import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from file_operations import browse_file, search_strings
from utils import close_window
from tooltip import ToolTip

# DPI Awareness for Windows (put this at the beginning)
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def create_gui():
    root = tk.Tk()
    root.title("Search App")

    # Set default font size
    font.nametofont("TkDefaultFont").configure(size=10)

    # Create main frame with padding
    main = ttk.Frame(root, padding=(30, 15))
    main.grid(sticky="EW")

    # Ensure columns expand properly
    root.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=1)  # Allow entry fields to expand

    search_strings_value = tk.StringVar()
    filename = tk.StringVar()

    # ROW 0
    # Header
    header = ttk.Label(
        main,
        text="Search for specific string(s) in dsx file",
        font=("Calibri", 16, "bold"),
    )
    header.grid(column=0, row=0, columnspan=3, pady=50)

    # ROW 1
    # Browse file label
    open_file_label = ttk.Label(main, text="Open File:", font=("Calibri", 12, "bold"))
    open_file_label.grid(column=0, row=1, sticky="W", padx=15, ipady=5)

    # Create Entry field to show file path
    file_entry = ttk.Entry(main, textvariable=filename, font=("Calibri", 12), width=50)
    file_entry.grid(column=1, row=1, sticky="EW", padx=15, ipady=5)
    ToolTip(
        file_entry,
        "Tooltip:\nBrowse for .dsx export file,\nwithin which you want to search for some value",
    )

    # Create Browse button
    browse_button = ttk.Button(
        main, text="Browse", command=lambda: browse_file(file_entry), cursor="hand2"
    )
    browse_button.grid(column=2, row=1, sticky="EW", padx=15, ipady=5)

    # ROW 2
    # Search string label
    search_strings_label = ttk.Label(
        main,
        text="Enter Search String(s):\n(comma delimited)",
        font=("Calibri", 12, "bold"),
    )
    search_strings_label.grid(column=0, row=2, sticky="W", padx=15, ipady=5)

    # Create Entry field for search string(s)
    search_strings_input = ttk.Entry(
        main, textvariable=search_strings_value, font=("Calibri", 12), width=50
    )
    search_strings_input.grid(column=1, row=2, sticky="EW", padx=15, ipady=5)
    ToolTip(
        search_strings_input,
        "Tooltip:\nEnter search string or strings.\nMust be delimited by comma.",
    )

    # ROW 3
    # Create Buttons Frame with full column width
    buttons_frame = ttk.Frame(main, padding=(30, 15))
    buttons_frame.grid(column=1, row=3, sticky="EW", padx=15, pady=50, ipady=5)

    # Make the frame's columns expand
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)

    # Create Search & Cancel Buttons with full width
    search_button = ttk.Button(
        buttons_frame,
        text="Search",
        cursor="hand2",
        command=lambda: search_strings(
            main, ttk.Label, status_label, search_strings_value, file_entry
        ),
    )
    search_button.grid(
        column=0, row=0, sticky="EW", padx=15, pady=10, ipady=5
    )  # Full width

    cancel_button = ttk.Button(
        buttons_frame, text="Close", cursor="hand2", command=lambda: close_window(root)
    )
    cancel_button.grid(
        column=1, row=0, sticky="EW", padx=15, pady=10, ipady=5
    )  # Full width

    # ROW 4
    # Status label (initially empty)
    status_label = ttk.Label(main, text="", font=("Calibri", 12, "bold"))
    status_label.grid(column=0, row=4, columnspan=3, pady=25, ipady=5)

    # Ensure buttons and entries match heights
    button_style = ttk.Style()
    button_style.configure(
        "TButton", padding=(10, 5)
    )  # (left/right, top/bottom padding)

    # Update to compute required width
    root.update_idletasks()  # Forces Tkinter to calculate the required size
    width = root.winfo_reqwidth()  # Get the required width

    # Set the geometry with fixed height but dynamic width
    root.geometry(f"{width}x800")
    root.mainloop()
