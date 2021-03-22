from collections import deque
from operator import attrgetter

#Perform the fifo
def fifo(jobs,num_frames):
    """ Frame list
    Each item in this list will be a tuple as follows:
    Tuple[0] - represents the number of the page frame sequentially, 1,2,3, etc..
    Tuple[1] - reresents the job current in this frame
    Tuple[2] - represents the moment that job arrived (starting with 0 for first moment
    """
    frame_list = []

    """
    A list to be returned to main GUI. This contains the results of the simulation so they can be displayed graphically
    """
    return_list=[]

    class __moment:
        def __init__(self,frames):
            self.frame=frames
    

    #initialize a list of frame, starting out with no jobs or moment
    for i in range((num_frames)):
        frame_list.append((i,None,None))

    #init the interrupts and moment
    inter  = 0
    moment = 0

    inter_list = []
    
    #iterate over each job in the list
    for job in jobs:
        did_inter = False
        #increment the time
        moment = moment + 1
        #if the job is not in a frame, need to place it
        if(not in_frame(job,frame_list)):
            #whenever a job is not in a frame, it is always an interupt
            inter = inter +1
            did_inter =True
            #represnts the index of the first free frame (-1 when memory full)
            target_frame = find_frame(frame_list)
            #if there is an emtpy frame, use it
            if(target_frame != -1):
                temp_num = frame_list[target_frame][0]
                temp_job = job
                frame_list[target_frame]=((temp_num,temp_job,moment))
            #otherwise we need to replace an exsisting frame's job
            else:
                target_frame = find_first(frame_list)
                temp_num = frame_list[target_frame][0]
                temp_job = job
                frame_list[target_frame]=((temp_num,temp_job,moment))

        if(did_inter):
            inter_list.append("*")
        else:
            inter_list.append(" ")
        
        for f in frame_list:
            return_list.append((moment,f[0]+1,f[1],did_inter))

        
    #return the list of events and also the failure rate
    return((return_list,round(inter/len(jobs),2),inter_list,inter))
    
#Perform the LRU
def lru(jobs,num_frames):

    #inner class to represent a job
    class __job:
        def __init__(self,name=None,time=0):
            self.name=name
            self.time=time
            
    #init list of empty job objects
    frame_list = [__job()]*num_frames
    return_list = []
    
    #init time and interrupt count
    moment = 0
    inter  = 0
    inter_list = []
    
    for job in jobs:
        #inc time
        moment = moment + 1
        
        did_inter = False

        #temp obj to easily set properties
        this_job = __job(job,moment)

        #if job already in a frame, increment its time
        if(in_frame_obj(this_job,frame_list)):
            index = frame_index(this_job,frame_list)
            frame_list[index]=__job(job,moment)
        
        #otherwise need to place job
        else:
            inter = inter +1
            did_inter =True
            #if theres a free page-frame, take it
            free_index = free_frame(frame_list)
            if(free_index != -1):
                frame_list[free_index]=__job(job,moment)
                
            #otherwise need to kick someone out
            else:
                min_time=min(frame_list,key=attrgetter('time'))
                index = frame_list.index(min_time)
                frame_list[index]=__job(job,moment)
                
        if(did_inter):
            inter_list.append("*")
        else:
            inter_list.append(" ")

        index = 1
        for f in frame_list:
            return_list.append((moment,index,f.name,did_inter))
            index = index +1 
    #return the list of events and also the failure rate
    return((return_list,round(inter/len(jobs),2),inter_list,inter))
   
            

#check if job is contained in any known job objects     
def in_frame_obj(job,frame_list):
    for frame in frame_list:
        if(job.name == frame.name):
            return True
    return False

#get frame index of job when using job object
def frame_index(job,frame_list):
    for frame in frame_list:
        if(job.name == frame.name):
            return frame_list.index(frame)
    return -1

#get first free frame when using job object
def free_frame(frame_list):
    for frame in frame_list:
        if(frame.name is None):
            return frame_list.index(frame)
    return -1
        
#linear search to check if a given job is in any page frames
def in_frame(job,frame_list):
    for frame in frame_list:
        if (frame[1] == job):
            return True
    return False

#returns the index of the first frame that has no current jobs
def find_frame(frame_list):
    for i in range(len(frame_list)):
        temp_frame = frame_list[i]
        if temp_frame[1] is None:
            return i
    return -1

#finds the job which arrived earliest based on its moment
def find_first(frame_list):
    temp_list = []
    for frame in frame_list:
        if(frame[1] != None and frame [2] != None):
            temp_list.append(frame)
    
    get_first_list = sorted(temp_list, key=lambda tup: tup[2])
    
    return frame_list.index(get_first_list[0])

    


