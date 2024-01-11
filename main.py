import ttkbootstrap as ttk
from PomodoroGUI import PomodoroGUI

class Run:
    @staticmethod
    def main():
        """
        Main function that creates the main window and starts the application.
        """
        root = ttk.Window(themename="superhero")
        app = PomodoroGUI(root)
        root.mainloop()

if __name__ == "__main__":
    Run.main()
