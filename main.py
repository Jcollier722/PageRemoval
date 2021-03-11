import sys 
sys.path.insert(0, 'menu/')

import tkinter as tk
import top_menu
import const
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        """Text variables for input"""
        self.job_entry = tk.StringVar()

        #make top menu frame
        top_menu.make_top(self,root)

        

        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Page Removal Simulator")
    root.resizable(width=False, height=False)
    root.geometry(const.DEF_SIZE)
    my_gui = GUI(root)
    root.mainloop()
