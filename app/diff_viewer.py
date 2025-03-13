import difflib
import tkinter as tk
from tkinter import ttk, scrolledtext


class DiffViewer:
    def __init__(self, root, old_code, new_code, title="Code Diff Viewer"):
        self.root = root
        self.root.title(title)
        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Courier", 10)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        diff_text = self.generate_diff(old_code, new_code)
        self.text_area.insert(tk.END, diff_text)
        self.text_area.config(state=tk.DISABLED)  # Make it read-only

    def generate_diff(self, old_code, new_code):
        """Generates a unified diff between old and new code."""
        old_lines = old_code.splitlines(keepends=True)
        new_lines = new_code.splitlines(keepends=True)

        diff = difflib.unified_diff(
            old_lines, new_lines, fromfile="Old Code", tofile="New Code", lineterm=""
        )
        return "".join(diff)


# Example usage:
if __name__ == "__main__":
    old_sample = """def old_function():
    print("Old Code")
"""

    new_sample = """def new_function():
    print("New Code")
"""

    root = tk.Tk()
    app = DiffViewer(root, old_sample, new_sample)
    root.mainloop()
