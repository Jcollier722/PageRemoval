import sys 
sys.path.insert(0, 'menu/')
sys.path.insert(1, 'util/')
sys.path.insert(2, 'sim/')

import tkinter as tk
import menu
import import_jobs as ij
import validate_jobs as validate
import show_results as sr
import pretty_print as pp
import compare_sim
import const
import generate
import simulation
import string
import random
from tkinter import ttk
from tkinter.filedialog import askopenfile


class GUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        """Text variables for input"""
        self.job_entry = tk.StringVar()
        
        self.job_list = None
        self.is_valid=False
        self.count = 0

        #init frame count to 1
        self.page_frame_count = 0

        #init coordinates for page frames to be rendered
        self.x = const.START_X
        self.y = const.START_Y

        #house generated labels so they can be removed later
        self.page_frame_labels = []

        #make top menu frame
        menu.make_top(self,root)
        menu.make_mid(self,root)
        menu.make_bottom(self,root)
    
    #callback to import jobs from a text file
    def import_jobs(self):
        file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
        self.job_list=(ij.import_j(file.name))
        self.is_valid=True
        self.job_entry.set("Jobs Imported")
        self.submit_button['state']='disabled'
        
     #callback to render a page frame box
    def make_box(self):
        if(self.page_frame_count < 5):
            this_text = "Page Frame "+str(self.page_frame_count+1)
            this_label = tk.Label(self.page_frame_grid,text=this_text,font= "arial 15 bold",borderwidth=3,relief='groove',pady=7,padx=10)
            this_label.place(relx=self.x,rely=self.y)
            self.page_frame_labels.append(this_label)
            self.page_frame_count = self.page_frame_count+1
            self.y = self.y +const.Y_INC
    
    #callback to de-redner a page frame
    def remove_box(self):
        if(self.page_frame_count > 2):
            this_label = self.page_frame_labels.pop()
            this_label.place_forget()
            self.page_frame_count = self.page_frame_count -1
            self.y = self.y -const.Y_INC

    #callback to submit jobs; this validates user input
    def submit_jobs(self):
        #get current user input
        user_input = self.job_entry.get()
        #validate it
        if(validate.validate_input(self,user_input)!=-1):
            self.job_list = None
            self.job_list = validate.validate_input(self,user_input)
            tk.messagebox.showinfo('Success', 'Jobs are valid.')
            self.is_valid=True
        else:
            tk.messagebox.showerror('Error', 'Invalid input. Seperate jobs by comma.')

    def run_sim(self):
        
        if(not (self.is_valid)):
            tk.messagebox.showerror('Error', 'Please enter valid jobs before submitting.')
            return
        
        """FIFO"""
        fifo_event = simulation.fifo(self.job_list,self.page_frame_count)
        events = fifo_event[0]
        self.fifo_inter = fifo_event[2]
        self.fifo_num_inter = fifo_event[3]
        self.fifo_events = pp.print_fifo(self.page_frame_count,events)
        
        """LRU"""
        lru_event=simulation.lru(self.job_list,self.page_frame_count)
        new_events = lru_event[0]
        self.lru_inter = lru_event[2]
        self.lru_num_inter = lru_event[3]
        self.lru_events = pp.print_fifo(self.page_frame_count,new_events)

        self.submit_button['state']='normal'
        
        #simulation.lru(self.job_list,self.page_frame_count)    
        self.new_window()
        
     
    def new_window(self):
        sr.make_results(self)

    def show_fifo(self):
        self.lru.place_forget()
        self.fifo.place(relx=0,rely=.10)

    def show_lru(self):
        self.fifo.place_forget()
        self.lru.place(relx=0,rely=.10)

    def compare_sim(self):
        compare_sim.compare(['FIFO','LRU'],[self.fifo_num_inter,self.lru_num_inter])

    def generate_job(self):
        generate.generate_jobs(self)
        
    def do_generation(self):
        #get the range for the sim
        gen_range = self.range_var.get()
        gen_size = self.size_var.get()
        left_bound = 0
        right_bound = gen_range[gen_range.index('-')+1:]
        right_bound = string.ascii_lowercase.index(right_bound.lower())
        
        file = open("my_simulation.txt","w+")

        for i in range(int(gen_size)):
            letter = random.randint(left_bound,right_bound)
            file.write(const.ALPHA[letter])
            file.write("\n")
        file.close()
        
        tk.messagebox.showinfo('Success', 'Simulation generated')
        self.window.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Page Removal Simulator")
    root.resizable(width=False, height=False)
    root.geometry(const.DEF_SIZE)
    my_gui = GUI(root)
    root.mainloop()
