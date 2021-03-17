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
       return -1
    
    #user must delimit with comma
    if(',' not in user_input):
        return -1

    #split input on comma
    user_input=user_input.split(',')

    return user_input
    
        
    
