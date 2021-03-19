#class to arrange tuple into easily printable lists
class frameEvents:
    def __init__(self,frame,event=None):
        self.frame=frame
        self.event=event

def print_fifo(page_frame_count,events):
        #keep a list of frame event objects
        frame_events_list = []
        
        #for each page frame, get the events that occured on that page frame
        for y in range(1,page_frame_count+1):

            #init frame object
            this_frame_event = frameEvents(y,[])

            #get the job identitifer
            #https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples
            temp_events = ([item for item in events if item[1] == y])

            #iterate over events and append each event to the frame objects event list
            for temp in temp_events:
                this_frame_event.event.append(temp[2])

            #append the frame object
            frame_events_list.append(this_frame_event)
    
        return frame_events_list
