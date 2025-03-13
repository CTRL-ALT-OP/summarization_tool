import tkinter as tk
from tkinter import ttk
from file_manager import FileManager
from version_control import VersionControl
from diff_viewer import DiffViewer
from summarizer import Summarizer
from api_handler import APIHandler
import config


class SummarizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Summarization Tool")
        self.root.geometry("800x600")

        # Initialize modules
        self.version_control = VersionControl(config.REPO_PATH)
        self.summarizer = Summarizer()
        self.api_handler = APIHandler(config.API_URL)

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons and UI elements
        self.setup_ui()

    def setup_ui(self):
        # Detect Changes Button
        self.detect_changes_button = ttk.Button(
            self.main_frame, text="Detect Changes", command=self.detect_changes
        )
        self.detect_changes_button.pack(pady=10)

        # Open File Manager Button
        self.open_file_manager_button = ttk.Button(
            self.main_frame, text="Open File Manager", command=self.open_file_manager
        )
        self.open_file_manager_button.pack(pady=10)

    def detect_changes(self):
        """Detects modified files and displays diffs."""
        modified_files = self.version_control.get_modified_files()
        if not modified_files:
            print("No changes detected.")
            return

        for file in modified_files:
            diff = self.version_control.get_file_diff(file)
            diff_window = tk.Toplevel(self.root)
            DiffViewer(diff_window, "", diff, title=f"Changes in {file}")

    def open_file_manager(self):
        """Opens the file manager for browsing and editing documentation."""
        file_manager_window = tk.Toplevel(self.root)
        FileManager(file_manager_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = SummarizationApp(root)
    root.mainloop()
