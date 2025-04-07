import os, subprocess

import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.font as font

from classes.gui.create_header import _create_header
from classes.gui.create_status_label import _create_status_label, _update_status_label
from classes.gui.create_browse_file_section import _create_browse_file_section
from classes.gui.create_search_section import _create_search_section
from classes.gui.create_buttons_section import _create_buttons_section
from classes.gui.create_open_results_section import (
    _create_open_results_section,
    _update_open_results_section,
)


class JobSearchGui:
    """
    Object that creates simple tkinter GUI for the app, asking user to provide path
    to the extracted .dsx file and comma-delimited search strings.
    Returns output file with the found jobs and provides message informing about
    the search progress.
    """

    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Search App")

        # widgets variables
        self.search_strings_var = tk.StringVar()
        self.filepath_var = tk.StringVar()

        self._setup_fonts()
        self._setup_widgets_layout()
        self._setup_layout()

    # Set default font size
    def _setup_fonts(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Calibri", size=12, weight="bold")

    # Set widgets styling
    def _setup_widgets_layout(self):
        button_style = ttk.Style()
        button_style.configure("TButton", padding=(30, 15))
        entry_style = ttk.Style()
        entry_style.configure("TEntry", padding=(5, 15))

    # Create main layout
    def _setup_layout(self):
        self.main_frame = ttk.Frame(self.root, padding=(30, 15))
        self.main_frame.grid(sticky="EW")

        # Ensure columns expand properly
        self.root.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)  # Allow entry fields to expand

        # Create sections - ROWs of grid
        _create_header(self)  # ROW 0
        self.file_entry = _create_browse_file_section(  # ROW 1
            self.main_frame, self.filepath_var, self.browse_file
        )
        self.search_entry = _create_search_section(  # ROW 2
            self.main_frame, self.search_strings_var
        )
        _create_buttons_section(  # ROW 3
            self.main_frame, self.on_search_click, self.close_window
        )
        self.status_lbl = _create_status_label(self.main_frame)  # ROW 4
        self.open_results_label = _create_open_results_section(self.main_frame)  # ROW 5

        # Set window size
        self.root.update_idletasks()  # Forces Tkinter to calculate the required size
        width = self.root.winfo_reqwidth()  # Get the required width
        height = self.root.winfo_reqheight()  # Get the required height
        self.root.geometry(f"{width}x{height}")

    def browse_file(self):
        path = filedialog.askopenfilename(title="Select a File")
        if path:
            self.filepath_var.set(path)

    # search for jobs
    def on_search_click(self):
        filepath = self.filepath_var.get()
        keywords = self.search_strings_var.get()

        if not os.path.isfile(filepath):
            _update_status_label(
                self.status_lbl,
                f"Error: Please select a valid file",
                "red",
            )
            return

        if not keywords:
            _update_status_label(
                self.status_lbl,
                f"Error: Enter at least 1 valid search string(s) delimited with comma",
                "red",
            )
            return

        try:
            # Update the status label to show "Search in progress"
            _update_status_label(self.status_lbl, "Search in progress...", "orange")
            # Clear the link to target path with results
            _update_open_results_section(
                self.open_results_label,
                "",
                None,
            )
            self.main_frame.update_idletasks()  # Update the GUI immediately

            loaded_file = self.controller.engine.load_file(filepath)
            keywords_lst = self.controller.engine.prepare_keywords(keywords)
            found_jobs = self.controller.engine.search_keywords(
                loaded_file, keywords_lst
            )
            target_folder = self.controller.engine.create_target_folder(filepath)
            self.controller.engine.write_results(target_folder, found_jobs)

            # Update status for success
            _update_status_label(
                self.status_lbl, "Process finished successfully!", "green"
            )

            # Update the link to target path with results
            _update_open_results_section(
                self.open_results_label,
                "Click here to open folder with the output file(s)",
                target_folder,
            )

        except Exception as e:
            _update_status_label(
                self.status_lbl,
                f"Error: Something went wrong: {e}",
                "red",
            )

    # Function to close the main window
    def close_window(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
