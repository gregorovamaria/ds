from classes.job_search_gui import JobSearchGui
from classes.job_search_engine import JobSearchEngine

# DPI Awareness for Windows (put this at the beginning)
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class JobSearchApp:
    def __init__(self):
        self.engine = JobSearchEngine()
        self.gui = JobSearchGui(self)

    def run(self):
        self.gui.run()


if __name__ == "__main__":
    app = JobSearchApp()
    app.run()
