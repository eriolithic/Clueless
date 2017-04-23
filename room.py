class connDirection(object):
    left = 0
    up = 1
    right = 2
    down = 3

    base = int('1111', 2)

class boardspace(object):

    #length = 0
    #width = 0
    #connectedTo = [None, None, None, None]

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.connectedTo = [None, None, None, None] #[left, up, right, down]
        print "in boardspace"

    def addConnection(self, position, connection):
        self.connectedTo[position] = connection

        print self.connectedTo


class room(boardspace):
    #length = 3
    #width = 3
    #connectedTo = [None, None, None, None]

    def __init__(self): #connections is an array
        print "in room"
        super(room,self).__init__(3,3)
        print "room length: " + str(self.length)

    

    
class hallway(boardspace):
    
    def __init__(self): #connections is an array
        print "in hallway"
        super(hallway,self).__init__(1,1)
        print "hallway length: " + str(self.length)

class gameboard(object):

    def __init__():
        study = room()
        hall = room()
        library = room()
        billiardRoom = room()
        diningRoom = room()
        conservatory = room()
        ballRoom = room()
        kitchen = room()

        hall1 = hallway()
        hall2 = hallway()
        hall3 = hallway()
        hall4 = hallway()
        hall5 = hallway()
        hall6 = hallway()
        hall7 = hallway()
        hall8 = hallway()
        hall9 = hallway()
        hall10 = hallway()
        hall11 = hallway()
        hall12 = hallway()

        study.addConnection(boardspace.right, hall1)
        study.addConnection(boardspace.down, hall3)



        print "in gameboard"
    
    def initialize():
        pass



if __name__ == '__main__':
    hallwayEx = hallway()
    roomEx = room()
    #roomEx = room(hallwayEx)
    #print roomEx.connectedTo

    #boardspaceEx = boardspace(1,1)
    #boardspaceEx.addConnection(boardspace.left, hallwayEx)

    #print boardspaceEx.length