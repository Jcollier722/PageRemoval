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


def make_results(self):
    self.count = self.count + 1
    self.window=tk.Toplevel(self)
    self.window.geometry("825x900")
    self.window.config(bg='#bfd7ff')
    self.window.resizable(width=False, height=False)
    
    root = self.window
    
    menu = tk.Canvas(root,width=815,height=const.MAX_HEIGHT/8,bg=const.BLUE,bd=2)
    menu.config(highlightbackground='black')
    menu.place(relx=0)

    #Title
    title = tk.Label(menu,text=const.RESULT_TITLE,font='arial 30 bold ',bg=const.BLUE).place(relx=.5,rely=0.40,anchor="center")

    #fifo frame
    fifo = tk.Canvas(root,width=815,height=const.MAX_HEIGHT/2,bg='red',bd=2)
    fifo.config(highlightbackground='black')
    fifo.place(relx=0,rely=.10)

    #fifo title
    title = tk.Label(fifo,text=const.FIFO_TITLE,font='arial 20 bold underline',bg=const.BLUE).place(relx=0.01,rely=0.10,anchor="w")

    fifo_y = const.START_Y+.10
    #print each page frame
    for i in range(self.page_frame_count):
        this_text = "Page Frame "+str(i+1)
        this_label = tk.Label(fifo,text=this_text,font= "arial 15 bold",borderwidth=3,relief='groove',pady=7,padx=10)
        this_label.place(relx=0.01,rely=fifo_y)
        fifo_y = fifo_y + (const.Y_INC-.02)

    """
    Lots of magic numbers here, will move to const.py if time allows for this assignment.
    """
    
    #print the jobs each page frame has at each moment
    y_fifo_jobs = const.START_Y+.10
    x_fifo_jobs = self.x+.17
    for i in range(self.page_frame_count):
        for event_list in self.fifo_events:
            if(str(event_list.frame) == str(i+1)):
                for e in event_list.event:
                    if e is None:
                        e="-"
                    tk.Label(fifo,text=str(e),font= "arial 10 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_fifo_jobs,rely=y_fifo_jobs)
                    x_fifo_jobs = x_fifo_jobs + .07
        y_fifo_jobs = y_fifo_jobs +0.15
        x_fifo_jobs = self.x+.17
    
    #lru frame
    lru = tk.Canvas(root,width=815,height=const.MAX_HEIGHT/2,bg='yellow',bd=2)
    lru.config(highlightbackground='black')
    lru.place(relx=0,rely=.50)

#Turn list into string and print nicely
def pretty_list(the_list):
    return_string = ""

    for item in the_list:
        if item is None:
            item = "empty"
        return_string = return_string + (item + "  ")
    return return_string
    
