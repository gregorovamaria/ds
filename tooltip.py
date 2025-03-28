import tkinter as tk
from tkinter import ttk


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        # Bind events to show and hide the tooltip
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        # Create a tooltip when mouse hovers over the widget
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 50  # Adjust position
        y += self.widget.winfo_rooty() + 50  # Adjust position

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Remove the window border
        self.tooltip.wm_geometry(f"+{x}+{y}")  # Position the tooltip

        label = ttk.Label(
            self.tooltip,
            text=self.text,
            background="lightyellow",
            relief="solid",
            padding=(15, 15),
        )
        label.pack()

    def hide_tooltip(self, event):
        # Hide the tooltip when mouse leaves the widget
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
