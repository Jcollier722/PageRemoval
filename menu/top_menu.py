import const
import tkinter as tk
from tkinter import ttk

"""This file creates the top menu bar and takes needed user input"""

def make_top(self, root):
    #top menu frame
    menu = tk.Canvas(root,width=const.MAX_WIDTH-10,height=const.MAX_HEIGHT/3,bg=const.BLUE,highlightthickness=5,highlightcolor='black')
    menu.place(relx=0)

    #Title
    title = tk.Label(menu,text=const.MAIN_TITLE,font='arial 25 bold ',bg=const.BLUE).place(relx=.5,rely=0.2,anchor="center")
    
    #input label
    entry_label = tk.Label(menu,text=const.ENTER_JOB,font='arial 12 bold',bg=const.BLUE).place(relx=0.05,rely=0.5,anchor="w")
    
    #entry box with text variable for job entry
    job_entry = tk.Entry(menu,textvariable=self.job_entry,width=50).place(relx=0.48,rely=0.5,anchor="w")
    

    #buttons
    import_button = tk.Button(menu,text=const.IMPORT_JOB,font='arial 12 bold',height=3,width=20,bg=const.GREEN).place(relx=0.1,rely=0.8,anchor="w")
    submit_button = tk.Button(menu,text=const.SUBMIT_JOB,font='arial 12 bold',height=3,width=20,bg=const.GREEN).place(relx=0.5,rely=0.8,anchor="w")
