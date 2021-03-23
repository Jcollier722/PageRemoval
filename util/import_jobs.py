"""This module parses a text file and creates jobs objects based on it"""

def import_j(path):
    return_list = []
    file = open(path,'r')
    lines = file.readlines()
    
    for line in lines:
        return_list.append(line.strip().upper())
        
    return return_list
