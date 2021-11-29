"""
Problem Statment
Design a meeting scheduler to book a meeting and return the name of the room booked

Goal(s) of the system
 ■ Book a room for the meeting and return the name of the room booked
 ■ History of the meetings booked
"""

from roomBooker import RoomBooker

def processCommand(string,bookerObj):
    cmdArr = string.split()

    if cmdArr[0] == "register_room":
        roomName = " ".join(cmdArr[1:])
        bookerObj.registerRoom(roomName)
    
    elif cmdArr[0] == "book_room":
        if len(cmdArr) == 4:
            bookerObj.bookRoom(cmdArr[1],cmdArr[2],cmdArr[3])
        
        else:
            roomName = " ".join(cmdArr[4:])
            bookerObj.bookRoom(cmdArr[1],cmdArr[2],cmdArr[3],roomName)

    elif cmdArr[0] == "get_history":
        roomName = " ".join(cmdArr[1:])
        bookerObj.getHistory(roomName)


booker = RoomBooker()

while True:

    string = input()

    if string == "exit":
        break 

    processCommand(string,booker)

