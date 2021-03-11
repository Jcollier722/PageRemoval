import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

#validate user job input
def validate_input(self,user_input):

    """check some edge cases"""
    #check if len of input is equal to or less than amount of frames
    #return if this is the case, no simulation needed here

    #user must enter jobs before submitting
    if(len(user_input) <= 0):
       mb.showerror('Error','Must enter jobs before submission!')
       return
    
    #user must delimit with comma
    if(',' not in user_input):
        mb.showerror('Error','You must seperate jobs by comma.')
        return

    
        
        
        
    
