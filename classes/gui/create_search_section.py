from tkinter import ttk
from classes.gui.create_tooltip import ToolTip


def _create_search_section(parent, search_strings_value_var):
    ttk.Label(parent, text="Enter Search String(s):\n(comma delimited)").grid(
        column=0, row=2, sticky="W", padx=15, ipady=5
    )

    # Create Entry field for search string(s)
    search_entry = ttk.Entry(
        parent,
        textvariable=search_strings_value_var,
        width=50,
    )
    search_entry.grid(column=1, row=2, sticky="EW", padx=15, ipady=5)

    ToolTip(
        search_entry,
        "Tooltip:\nEnter search string or strings.\nMust be delimited by comma.",
    )

    return search_entry
