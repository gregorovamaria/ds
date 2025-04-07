from tkinter import ttk


def _create_buttons_section(parent, search_fn, close_window_fn):
    # Create Buttons Frame with full column width
    buttons_frame = ttk.Frame(parent)
    buttons_frame.grid(column=1, row=3, sticky="EW", padx=15, pady=50, ipady=5)

    # Make the frame's columns expand
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)

    # Create Search & Cancel Buttons with full width
    ttk.Button(
        buttons_frame,
        text="Search",
        cursor="hand2",
        command=search_fn,
    ).grid(
        column=0, row=0, sticky="EW", padx=15, pady=10, ipady=5
    )  # Full width

    ttk.Button(
        buttons_frame, text="Close", cursor="hand2", command=close_window_fn
    ).grid(
        column=1, row=0, sticky="EW", padx=15, pady=10, ipady=5
    )  # Full width
