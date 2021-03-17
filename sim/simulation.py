from collections import deque


#Perform the fifo
def fifo(jobs,num_frames):

    """ Frame list
    Each item in this list will be a tuple as follows:
    Tuple[0] - represents the number of the page frame sequentially, 1,2,3, etc..
    Tuple[1] - reresents the job current in this frame
    Tuple[2] - represents the moment that job arrived (starting with 0 for first moment
    """
    frame_list = []

    #initialize a list of frame, starting out with no jobs or moment
    for i in range((num_frames)):
        frame_list.append((i,None,None))

    #init the interrupts and moment
    inter  = 0
    moment = 0

    #iterate over each job in the list
    for job in jobs:

        #increment the time
        moment = moment + 1

        #if the job is not in a frame, need to place it
        if(not in_frame(job,frame_list)):
            #whenever a job is not in a frame, it is always an interupt
            inter = inter +1

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
            
        
        for f in frame_list:
            print(f[0],f[1],f[2])
        print()

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
