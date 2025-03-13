import tkinter as tk
from gui import SummarizationApp


def main():
    root = tk.Tk()
    app = SummarizationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
