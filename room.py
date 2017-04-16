class boardspace(object):
    left = 0
    up = 1
    right = 2
    down = 3

    #length = 0
    #width = 0
    #connectedTo = [None, None, None, None]

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.connectedTo = [None, None, None, None] #[left, up, right, down]
        

    def addConnection(self, position, connection):
        self.connectedTo[position] = connection
        print self.connectedTo


class room(object):
    length = 3
    width = 3
    connectedTo = [None, None, None, None]

    def __init__(self, connections = None): #connections is an array
        self.connectedTo = connections

    
class hallway(object):
    length = 1
    width = 1
    def __init__(self, connections = None):
        self.connectedTo = connections

class gameboard(object):
    study = room()
    library = room()
    
    def initialize():
        pass



if __name__ == '__main__':
    hallwayEx = hallway()
    #roomEx = room(hallwayEx)
    #print roomEx.connectedTo

    boardspaceEx = boardspace(1,1)
    boardspaceEx.addConnection(boardspace.left, hallwayEx)

    print boardspaceEx.length