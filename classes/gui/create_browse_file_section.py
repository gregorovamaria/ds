from tkinter import ttk
from classes.gui.create_tooltip import ToolTip


def _create_browse_file_section(parent, filename_var, browse_file):
    ttk.Label(parent, text="Open File:").grid(
        column=0, row=1, sticky="W", padx=15, ipady=5
    )

    file_entry = ttk.Entry(parent, textvariable=filename_var, width=50)
    file_entry.grid(column=1, row=1, sticky="EW", padx=15, ipady=5)

    ToolTip(
        file_entry,
        "Tooltip:\nBrowse for .dsx export file,\nwithin which you want to search for some value",
    )

    ttk.Button(parent, text="Browse", command=browse_file, cursor="hand2").grid(
        column=2, row=1, sticky="EW", padx=15, ipady=5
    )

    return file_entry
