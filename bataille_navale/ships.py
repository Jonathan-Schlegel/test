class Ship():
    def __init__(self, type, size, coordonnees = (0,0), orientation = None):
        self.type = type
        self.size = size
        self.orientation = orientation
        self.coordonnees = coordonnees
        self.use = False

    def getType(self):
        return self.type
    
    def getSize(self):
        return self.size
    
    def getOrientation(self):
        return self.orientation
    
    def getCoordonnees(self):
        return self.coordonnees




