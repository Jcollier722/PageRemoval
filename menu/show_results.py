"""This file is the results window"""
import sys 
sys.path.insert(0, 'menu/')
sys.path.insert(1, 'util/')
sys.path.insert(2, 'sim/')
import tkinter as tk
import menu
import import_jobs as ij
import validate_jobs as validate
import show_results as sr
import const
import simulation
from tkinter import ttk
from tkinter.filedialog import askopenfile

class NewWindow(tk.Toplevel):
    
    def __init__(self, master = None):
        super().__init__(master = master)  
        self.geometry("750x750") 
        self.title("Page Removal Simulator")
        self.resizable(width=False, height=False)

        
              
        #alias self to root to make life easier
        root = self
        
        menu = tk.Canvas(root,width=const.MAX_WIDTH+41,height=const.MAX_HEIGHT/8,bg=const.BLUE,bd=2)
        menu.config(highlightbackground='black')
        menu.place(relx=0)

        #Title
        title = tk.Label(menu,text=const.RESULT_TITLE,font='arial 30 bold ',bg=const.BLUE).place(relx=.5,rely=0.40,anchor="center")

        #fifo frame
        fifo = tk.Canvas(root,width=const.MAX_WIDTH+41,height=const.MAX_HEIGHT/2.5,bg='red',bd=2)
        fifo.config(highlightbackground='black')
        fifo.place(relx=0,rely=.14)

        #lru frame
        lru = tk.Canvas(root,width=const.MAX_WIDTH+41,height=const.MAX_HEIGHT/2.5,bg='yellow',bd=2)
        lru.config(highlightbackground='black')
        lru.place(relx=0,rely=.54)
