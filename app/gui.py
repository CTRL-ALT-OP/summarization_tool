import tkinter as tk
from tkinter import ttk


class SummarizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Summarization Tool")
        self.root.geometry("800x600")

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Placeholder Label
        self.label = ttk.Label(
            self.main_frame,
            text="Welcome to the Summarization Tool",
            font=("Arial", 14),
        )
        self.label.pack(pady=20)

        # Placeholder for buttons and other UI elements
        self.setup_ui()

    def setup_ui(self):
        # Example Button
        self.detect_changes_button = ttk.Button(
            self.main_frame, text="Detect Changes", command=self.detect_changes
        )
        self.detect_changes_button.pack(pady=10)

    def detect_changes(self):
        # Placeholder function for detecting file changes
        print("Detecting changes...")
