import const
import tkinter as tk
from tkinter import ttk

"""This file creates the top menu bar and takes needed user input"""

def make_top(self, root):
    #top menu frame
    menu = tk.Canvas(root,width=const.MAX_WIDTH-10,height=const.MAX_HEIGHT/3,bg=const.BLUE,bd=2)
    menu.config(highlightbackground='black')
    menu.place(relx=0)

    #Title
    title = tk.Label(menu,text=const.MAIN_TITLE,font='arial 25 bold ',bg=const.BLUE).place(relx=.5,rely=0.2,anchor="center")
    
    #input label
    entry_label = tk.Label(menu,text=const.ENTER_JOB,font='arial 12 bold',bg=const.BLUE).place(relx=0.05,rely=0.5,anchor="w")
    
    #entry box with text variable for job entry
    job_entry = tk.Entry(menu,textvariable=self.job_entry,width=50).place(relx=0.48,rely=0.5,anchor="w")
    
    #buttons
    import_button = tk.Button(menu,text=const.IMPORT_JOB,font='arial 12 bold',height=3,width=15,bg=const.GREEN,command=self.import_jobs).place(relx=0.17,rely=0.8,anchor="w")
    generate_button = tk.Button(menu,text=const.GENERATE_JOB,font='arial 12 bold',height=3,width=15,bg=const.GREEN,command=self.generate_job).place(relx=0.41,rely=0.8,anchor="w")
    self.submit_button = tk.Button(menu,text=const.SUBMIT_JOB,font='arial 12 bold',height=3,width=15,bg=const.GREEN,command=self.submit_jobs)
    self.submit_button.place(relx=0.65,rely=0.8,anchor="w")
    
def make_mid(self, root):
    #top menu frame
    mid_menu = tk.Canvas(root,width=const.MAX_WIDTH-10,height=const.MAX_HEIGHT/2,bg=const.BLUE,bd=2)
    mid_menu.config(highlightbackground='black')
    mid_menu.place(relx=0,rely=.35)

    #buttons
    add_button = tk.Button(mid_menu,text=const.ADD_PAGE,font='arial 12 bold',height=3,width=20,bg=const.GREEN,command=self.make_box).place(relx=0.17,rely=0.87,anchor="w")
    remove_button = tk.Button(mid_menu,text=const.REMOVE_PAGE,font='arial 12 bold',height=3,width=20,bg=const.GREEN,command=self.remove_box).place(relx=0.48,rely=0.87,anchor="w")

    #frame to contain page frame graphics
    self.page_frame_grid = tk.Canvas(mid_menu,width=const.MAX_WIDTH-10,height=(const.MAX_HEIGHT/2)-90,bg=const.BLUE,bd=2)
    self.page_frame_grid.place(relx=0)
    self.page_frame_grid.config(highlightbackground='black')

    #make the first 2 page frames
    self.make_box()
    self.make_box()

def make_bottom(self, root):
     #submit botton
     submit_button = tk.Button(root,text=const.START,font='arial 12 bold',height=4,width=68,bg=const.DGREEN,command=self.run_sim,borderwidth=2)
     submit_button.place(relx=0.005,rely=0.93,anchor="w")
