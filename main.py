import tkinter as tk
from tkinter import ttk

class GUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Page Removal Simulator")
    root.resizable(width=False, height=False)
    root.geometry("700x700")
    my_gui = GUI(root)
    root.mainloop()
