from tkinter import ttk


def _create_header(self):
    ttk.Label(
        self.main_frame,
        text="Search for specific string(s) in dsx file",
        font=("Calibri", 16, "bold"),
    ).grid(column=0, row=0, columnspan=3, pady=50)
