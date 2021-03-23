import sys 
sys.path.insert(0, 'menu/')
sys.path.insert(1, 'util/')
sys.path.insert(2, 'sim/')
import tkinter as tk
import menu
import import_jobs as ij
import validate_jobs as validate
import show_results as sr
import export_results as xr
import compare_sim 
import const
import simulation
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

def generate_jobs(self):
    self.count = self.count + 2
    self.window=tk.Toplevel(self)
    self.window.geometry("500x300")
    self.window.config(bg='#bfd7ff')
    self.window.resizable(width=False, height=False)

    self.window

    my_title = tk.Label(self.window,text="Job Generation",font='arial 18 bold underline',bg=const.BLUE).place(relx=0.35,rely=0.05)
    range_label = tk.Label(self.window,text=const.RANGE,font='arial 12 bold ',bg=const.BLUE).place(relx=0.02,rely=0.30)
    size_label = tk.Label(self.window,text=const.SIZE,font='arial 12 bold ',bg=const.BLUE).place(relx=0.02,rely=0.50)

    self.range_var = tk.StringVar()
    self.size_var = tk.StringVar()
    
    range_entry = tk.Entry(self.window,textvariable=self.range_var,width=30).place(relx=0.45,rely=0.30)
    size_entry = tk.Entry(self.window,textvariable=self.size_var,width=30).place(relx=0.45,rely=0.50)

    submit = tk.Button(self.window,text='Generate',font='arial 12 bold ',height=2,width=10,bg=const.GREEN,command=self.do_generation).place(relx=0.40,rely=0.80)
    
    
