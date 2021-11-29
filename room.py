from collections import defaultdict 

class Room:
    def __init__(self,name):
        self.name = name 
        self.currentBookings = defaultdict(list) 
        self.history = defaultdict(list)

    def printHistory(self):

        if len(self.history) == 0:
            print("No booking were made")
        
        else:
            for date in self.history:
                
                currBookings = []
                
                for booking in self.history[date]:
                    currBookings.append("-".join(booking))
                
                print("Room name",self.name,"was booked on",date,"for hours =",",".join(currBookings))
            


        


