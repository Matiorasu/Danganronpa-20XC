import random

end = 0
investigate = 0
nextMove = "none"
room = "Lobby"

schoolRooms = ("Office","Lobby","Dressing Room","Auditorium","Entrance Hall")

class Character(object):
  def __init__(self, name, startingRoom):
    self.name = name
    self.room = startingRoom
  def randomlyMove(self):
    selfMove = random.randint(0,4)
    self.room = schoolRooms[selfMove]

    
    print(self.name + " is in the " + self.room)

jet = Character('Jet', 'lobby')
amy = Character('Amy','dressingRoom')
victor = Character('Victor','entranceHall')
edmund = Character('Edmund','office')
sarah = Character('Sarah','auditorium')
max = Character('Max','lobby')

    

def sameRoom(self):
        if self.room == room:
            print(self.name + " is in this room.")


while (end == 0 and investigate == 0):

        print("Each room has a corredsponding number: \n0: Main Office \n1: Lobby \n2: Dressing Room\n3: Auditorium \n4: Entrance Hall")
        direction = int(input("Where do you want to go?"))
        if direction > -1 and direction < 5:
            room = schoolRooms[direction]
            print("You are in the " + room + ".")
        else:
            print("Input invalid. Make sure you've entered a number that corresponds to an existing room!")
            print("You are in the " + room + ".")

        jet.randomlyMove()
        amy.randomlyMove()
        max.randomlyMove()
        sarah.randomlyMove()
        edmund.randomlyMove()
        victor.randomlyMove()
        sameRoom(jet)
        sameRoom(amy)
        sameRoom(max)
        sameRoom(sarah)
        sameRoom(edmund)
        sameRoom(victor)
