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
import export_results as xr
import const
import simulation
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile 

def make_results(self):

    if(len(self.job_list)>11):
        tk.messagebox.showwarning('Warning','Your job list is large and will be exported to a spreadsheet instead. Please select a save location.')
        files = [('Spreadsheet','.xlsx')]
        path  = asksaveasfile(filetypes = files, defaultextension = files)  
        xr.export(path,self.fifo_events,self.fifo_inter,self.lru_events,self.lru_inter,self.job_list)
        return
        


    
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
    fifo_view = tk.Button(menu,text=const.FIFO_TITLE,font='arial 12 bold',height=1,width=10,bg=const.GREEN,command=self.show_fifo).place(relx=0.3,rely=0.75,anchor="w")
    lru_view = tk.Button(menu,text=const.LRU_TITLE,font='arial 12 bold',height=1,width=10,bg=const.GREEN,command=self.show_lru).place(relx=0.58,rely=0.75,anchor="w")

    
    #fifo frame
    self.fifo = tk.Canvas(root,width=815,height=const.MAX_HEIGHT/1,bg=const.BLUE,bd=2)
    fifo = self.fifo
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
        fifo_y = fifo_y + 0.07

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
        y_fifo_jobs = y_fifo_jobs +0.07
        x_fifo_jobs = self.x+.17

    #move jobs to right of labels
    x_fifo_jobs = self.x+.17

    y_fifo_jobs = y_fifo_jobs +0.05
    
    tk.Label(fifo,text=const.REQ,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=0.01,rely=y_fifo_jobs)
    
    for job in self.job_list:
        tk.Label(fifo,text=str(job),font= "arial 10 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_fifo_jobs,rely=y_fifo_jobs)
        x_fifo_jobs = x_fifo_jobs + .07
        
    x_fifo_jobs = self.x+.17
    y_fifo_jobs=y_fifo_jobs +0.07
    tk.Label(fifo,text=const.INTER,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=40).place(relx=0.01,rely=y_fifo_jobs)

    for inter in self.fifo_inter:
        tk.Label(fifo,text=str(inter),font= "arial 13 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_fifo_jobs,rely=y_fifo_jobs)
        x_fifo_jobs = x_fifo_jobs + .07

    y_fifo_jobs=y_fifo_jobs +0.07
    x_fifo_jobs = self.x+.17
    tk.Label(fifo,text=const.TIME,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=15).place(relx=0.01,rely=y_fifo_jobs)

    for i in range(len(self.job_list)):
        tk.Label(fifo,text=str(i+1),font= "arial 11 ",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_fifo_jobs,rely=y_fifo_jobs)
        x_fifo_jobs = x_fifo_jobs + .07


    #lru frame
    self.lru = tk.Canvas(root,width=815,height=const.MAX_HEIGHT/1,bg=const.BLUE,bd=2)
    lru = self.lru
    lru.config(highlightbackground='black')
    #lru.place(relx=0,rely=.10)

    #lru title
    title = tk.Label(lru,text=const.LRU_TITLE,font='arial 20 bold underline',bg=const.BLUE).place(relx=0.01,rely=0.10,anchor="w")
    
    lru_y = const.START_Y+.10
    #print each page frame
    for i in range(self.page_frame_count):
        this_text = "Page Frame "+str(i+1)
        this_label = tk.Label(lru,text=this_text,font= "arial 15 bold",borderwidth=3,relief='groove',pady=7,padx=10)
        this_label.place(relx=0.01,rely=lru_y)
        lru_y = lru_y + 0.07

    """
    Lots of magic numbers here, will move to const.py if time allows for this assignment.
    """
    
    #print the jobs each page frame has at each moment
    y_lru_jobs = const.START_Y+.10
    x_lru_jobs = self.x+.17
    for i in range(self.page_frame_count):
        for event_list in self.lru_events:
            if(str(event_list.frame) == str(i+1)):
                for e in event_list.event:
                    if e is None:
                        e="-"
                    tk.Label(lru,text=str(e),font= "arial 10 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_lru_jobs,rely=y_lru_jobs)
                    x_lru_jobs = x_lru_jobs + .07
        y_lru_jobs = y_lru_jobs +0.07
        x_lru_jobs = self.x+.17

    #move jobs to right of labels
    x_lru_jobs = self.x+.17

    y_lru_jobs = y_lru_jobs +0.05
    
    tk.Label(lru,text=const.REQ,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=0.01,rely=y_lru_jobs)
    
    for job in self.job_list:
        tk.Label(lru,text=str(job),font= "arial 10 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_lru_jobs,rely=y_lru_jobs)
        x_lru_jobs = x_lru_jobs + .07
        
    x_lru_jobs = self.x+.17
    y_lru_jobs=y_lru_jobs +0.07
    tk.Label(lru,text=const.INTER,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=40).place(relx=0.01,rely=y_lru_jobs)

    for inter in self.lru_inter:
        tk.Label(lru,text=str(inter),font= "arial 13 bold",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_lru_jobs,rely=y_lru_jobs)
        x_lru_jobs = x_lru_jobs + .07

    y_lru_jobs=y_lru_jobs +0.07
    x_lru_jobs = self.x+.17
    tk.Label(lru,text=const.TIME,font= "arial 12 bold",borderwidth=3,relief='groove',pady=7,padx=15).place(relx=0.01,rely=y_lru_jobs)

    for i in range(len(self.job_list)):
        tk.Label(lru,text=str(i+1),font= "arial 11 ",borderwidth=3,relief='groove',pady=7,padx=10).place(relx=x_lru_jobs,rely=y_lru_jobs)
        x_lru_jobs = x_lru_jobs + .07


    
