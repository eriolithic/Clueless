class Direction(object):
    left = 0
    up = 1
    right = 2
    down = 3

    @staticmethod
    def opposite(position):
        base = int('11', 2)
        oppositeDir = (position + 2) & base

        print "oppositeDir: " + str(oppositeDir)
        return oppositeDir

class BoardSpace(object):

    #length = 0
    #width = 0
    #connectedTo = [None, None, None, None]

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.connectedTo = [None, None, None, None] #[left, up, right, down]
        #print "in boardspace"

    def addConnection(self, position, connection):
        self.connectedTo[position] = connection
        connection.connectedTo[Direction.opposite(position)] = self

        print "self.connectedTo: " + str(self.connectedTo)
        print "connection.connectedTo " + str(connection.connectedTo)


class Room(BoardSpace):
    #length = 3
    #width = 3
    #connectedTo = [None, None, None, None]

    def __init__(self): #connections is an array
        #print "in Room"
        super(Room,self).__init__(3,3)
        #print "Room length: " + str(self.length)

    def print(self):
        for i in range(self.length):
            for j in range(self.width):
                print "+"

    
class Hallway(BoardSpace):
    
    def __init__(self): #connections is an array
        #print "in Hallway"
        super(Hallway,self).__init__(1,1)
        #print "Hallway length: " + str(self.length)

    def print(self):
        for connection in connectedTo:
            if connection == None:
                print " "

class GameBoard(object):

    def __init__(self):
        self.sideLength = 11
        self.board = [[ 0 for x range(sideLength) for y in range(sideLength) ]]
        print "in gameboard"
    
    def printBoard(self):
        

    def initialize():
        study = Room()
        hall = Room()
        library = Room()
        lounge = Room()
        billiardRoom = Room()
        diningRoom = Room()
        conservatory = Room()
        ballRoom = Room()
        kitchen = Room()

        hallway1 = Hallway()
        hallway2 = Hallway()
        hallway3 = Hallway()
        hallway4 = Hallway()
        hallway5 = Hallway()
        hallway6 = Hallway()
        hallway7 = Hallway()
        hallway8 = Hallway()
        hallway9 = Hallway()
        hallway10 = Hallway()
        hallway11 = Hallway()
        hallway12 = Hallway()

        study.addConnection(Direction.right, hallway1)
        study.addConnection(Direction.down, hallway3)

        hall.addConnection(Direction.left, hallway1)
        hall.addConnection(Direction.right, hallway2)
        hall.addConnection(Direction.down, hallway4)
        
        lounge.addConnection(Direction.left, hallway2)
        lounge.addConnection(Direction.down, hallway5)

        library.addConnection(Direction.up, hallway3)
        library.addConnection(Direction.right, hallway6)
        library.addConnection(Direction.down, hallway8)

        billiardRoom.addConnection(Direction.left, hallway6)
        billiardRoom.addConnection(Direction.up, hallway4)
        billiardRoom.addConnection(Direction.right, hallway7)
        billiardRoom.addConnection(Direction.down,hallway9)

        diningRoom.addConnection(Direction.up, hallway5)
        diningRoom.addConnection(Direction.left, hallway7)
        diningRoom.addConnection(Direction.down, hallway10)

        conservatory.addConnection(Direction.up, hallway8)
        conservatory.addConnection(Direction.right, hallway11)

        ballRoom.addConnection(Direction.left, hallway11)
        ballRoom.addConnection(Direction.up, hallway9)
        ballRoom.addConnection(Direction.right, hallway12)

        kitchen.addConnection(Direction.left, hallway12)
        kitchen.addConnection(Direction.up, hallway10)




if __name__ == '__main__':
    gameBoard = GameBoard()