from room import Room 

class RoomBooker:

    def __init__(self):
        self.roomdict = {}

    def registerRoom(self,name):

        if name in self.roomdict:
            print("Room already exists!")
            return 

        # the room name is converted to lower case to avoid any redundancies or bad duplicates
        name = name.lower()
        currRoom = Room(name)
        self.roomdict[name] = currRoom

        print("Room name",currRoom.name,"was sucessfully registered!")

    def bookRoom(self,fromTime,toTime,date,name=None):
        
        if name == None:
            self.bookAnyRoom(fromTime,toTime,date)
        
        else:
            name = name.lower()
            self.bookByName(fromTime,toTime,date,name)
        
    def isClashing(self,start1,end1,start2,end2):
        
        if (start1 >= start2 and start1 <= end2) or (end1 >= start2 and end1 <= end2):
            return True 
        
        elif (start2 >= start1 and start2 <= end1) or (end2 >= start1 and end2 <= end1):
            return True 
        
        return False

    def bookAnyRoom(self,currFromTime,currToTime,currDate):
        
        for roomName in self.roomdict:
            currRoom = self.roomdict[roomName]

            if currDate in currRoom.currentBookings:
                for bookedFrom,bookedTo in currRoom.currentBookings[currDate]:

                    if self.isClashing(currFromTime,currToTime,bookedFrom,bookedTo) == False:
                        currRoom.currentBookings[currDate].append([currFromTime,currToTime])
                        currRoom.history[currDate].append([currFromTime,currToTime])

                        print("Room name",currRoom.name,"booked successfully from",currFromTime,"till",currToTime,"on",currDate)
                        return 
                
            else:
                currRoom.currentBookings[currDate].append([currFromTime,currToTime])
                currRoom.history[currDate].append([currFromTime,currToTime])

                print("Room name",currRoom.name,"booked successfully from",currFromTime,"till",currToTime,"on",currDate)
                return


        print("No room was available for time range",currFromTime,currToTime,"on",currDate)

    def bookByName(self,currFromTime,currToTime,currDate,name):
        
        if name not in self.roomdict:
            print("Invalid Name!")
        
        else:
            currRoom = self.roomdict[name]

            if currDate in currRoom.currentBookings:
                for bookedFrom,bookedTo in currRoom.currentBookings[currDate]:
                    if self.isClashing(currFromTime,currToTime,bookedFrom,bookedTo) == True:
                        print(currRoom.name,"is not available for the given time")
                        return 

            currRoom.currentBookings[currDate].append([currFromTime,currToTime])
            currRoom.history[currDate].append([currFromTime,currToTime])
            
            print("Room name",currRoom.name,"booked successfully from",currFromTime,"till",currToTime,"on",currDate)

    def getHistory(self,roomName):

        if roomName not in self.roomdict:
            print("Invalid room name")
        
        else:
            currRoom = self.roomdict[roomName]
            currRoom.printHistory()
        
