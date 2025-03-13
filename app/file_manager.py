import tkinter as tk
from tkinter import filedialog, ttk
import os


class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("600x400")

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # File List
        self.file_listbox = tk.Listbox(self.main_frame)
        self.file_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

        # Buttons
        self.load_button = ttk.Button(
            self.main_frame, text="Load Documentation", command=self.load_documentation
        )
        self.load_button.pack(pady=5)

        self.open_button = ttk.Button(
            self.main_frame, text="Open Selected File", command=self.open_file
        )
        self.open_button.pack(pady=5)

        self.populate_file_list()

    def populate_file_list(self):
        """Loads the list of documentation files from the documentation folder."""
        doc_path = "storage/documentation"  # Ensure this path is configurable later
        if not os.path.exists(doc_path):
            os.makedirs(doc_path)

        self.file_listbox.delete(0, tk.END)
        for file in os.listdir(doc_path):
            if file.endswith(".md"):  # Only show Markdown files
                self.file_listbox.insert(tk.END, file)

    def load_documentation(self):
        """Manually refresh the file list."""
        self.populate_file_list()

    def open_file(self):
        """Opens the selected Markdown file for editing."""
        selected_index = self.file_listbox.curselection()
        if not selected_index:
            return

        filename = self.file_listbox.get(selected_index)
        filepath = os.path.join("storage/documentation", filename)

        # Open the file editor
        editor_window = tk.Toplevel(self.root)
        editor_window.title(f"Editing: {filename}")
        editor_window.geometry("700x500")

        text_area = tk.Text(editor_window, wrap=tk.WORD)
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        with open(filepath, "r", encoding="utf-8") as file:
            text_area.insert(tk.END, file.read())

        def save_changes():
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(text_area.get("1.0", tk.END))
            editor_window.destroy()

        save_button = ttk.Button(
            editor_window, text="Save Changes", command=save_changes
        )
        save_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileManager(root)
    root.mainloop()
