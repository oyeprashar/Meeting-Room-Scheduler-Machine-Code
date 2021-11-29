# Meeting Room Scheduler Machine Code

## Contents of this readme
- Class Diagram
- Input/Ouput format
- Sample inputs

### The Class Diagram for the design:
![](/UMLClassDiagram.png)

# INPUT / OUTPUT FORMAT 

### 1. Registering a room:
- input: register_room <room_name> 
- output: Room name <room_name> was sucessfully registered!

### 2. Booking a room
- input type1: book_room <startTime> <end_time> <date> <room_name>
- output = Room name <room_name> booked successfully from <startTime> till <end_time> on <date> 

- input type1: book_room <startTime> <end_time> <date> 
- output = Room name <room_name> booked successfully from <startTime> till <end_time> on <date> 
  
### 3. Geting history of a room
- input: get_history <room_name>
- output: No bookings were made 
          On <date> bookings made were <list of comma seperated time ranges)

### 4. we stop taking input untill the "exit" is ecountered 


# Sample input 

### sample input - 1
```
register_room the pool room
register_room birthday room
book_room 1030 1230 29/11/2021 birthday room
book_room 1235 1240 29/11/2021 birthday room
book_room 1030 1230 1/12/2021 birthday room
book_room 1030 1230 2/12/2021 the pool room
book_room 1030 1230 3/12/2021 the pool room
get_history birthday room
get_history the pool room
exit
````

### sample input - 2 
```
register_room birthday room
register_room the pool room
book_room 1030 1230 29/11/2021 birthday room
book_room 1030 1230 29/11/2021 the pool room
book_room 1030 1230 29/11/2021
book_room 1300 1400 29/11/2021
get_history birthday room
get_history the pool room
exit
```

### sample input - 3 
```
register_room the pool room
register_room birthday room
get_history birthday room
get_history the pool room
exit
```
                                             
### sample input - 4 
```
register_room the pool room
register_room the pool room
exit
```
                                             
### sample input - 5 
```
register_room the pool room
register_room main room
book_room 1030 1230 29/11/2021
book_room 1030 1230 29/11/2021
exit
```
