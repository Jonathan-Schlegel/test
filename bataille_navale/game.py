from colored import Style, Fore, Back
from ships import Aircraft_carrier, Cruiser, Submarine, Torpedo_boat, ships_dict
import typing


class Grid:
    """Classe comprenant les méthodes et attributs liés à la grille du joueur"""
    grid : list = []
    ships_dict : dict = ships_dict

    def __init__(self):
        pass
        

    def save(self):
        """Sauvegarde la partie en cours"""
        pass

    def read(self, name_file):
        """Lit une partie sauvegardée"""
        pass

    def display(self):
        """Affiche la grille"""
        print("  A B C D E F G H I J")
        for x in range(8):
            print(x+1, end=" ")
            for y in range(10):
                print(self.grid[x][y], end=" ")
            print()
        print()

    def create(self):
        """Créé une grille vide"""
        grid = []
        for x in range(8):
            my_list= ["-" for y in range(10)]
            grid.append(my_list)
        self.grid = grid
        
    def getCoordonnees(self):
        """Récupère les coordonnées du coup"""
        print("Entrez les coordonnées: ",end="")
        return input()
    
    def testEndGame(self, sunk_ships : int) -> bool:
        """Vérifie si la partie est terminée"""
        if sunk_ships < 19:
            return True
        else:
            return False

    def placeShipVertical(self, ship : str, coordonnees : tuple):
        """Place un bateau verticalement"""
        size = self.ships_dict[ship]
        for x in range(size):
            self.grid[coordonnees[1]+x][coordonnees[0]] = ship
    
    def placeShipHorizontal(self, ship, coordonnees):
        """Place un bateau horizontalement"""
        size = self.ships_dict[ship]
        for x in range(size):
            self.grid[coordonnees[1]][coordonnees[0]+x] = ship

    def testPlaceVertical(self, ship: str, coordonnees : tuple):
        """Vérifie si un bateau peut être placé verticalement"""
        test : bool = True
        if self.ships_dict[ship] + int(coordonnees[1]) > 8:
            test = False
        for x in range(-1,2):
                for y in range(-1,self.ships_dict[ship]+1):
                    if self.grid[coordonnees[1]+y][coordonnees[0]+x] != "-":
                        test = False
        return test

    def testPlaceHorizontal(self, ship, coordonnees):
        """Vérifie si un bateau peut être placé horizontalement"""
        test : bool = True
        if self.ships_dict[ship] + int(coordonnees[0]) > 10:
            test = False
        for y in range(-1,2):
                for x in range(-1,self.ships_dict[ship]+1):
                    if self.grid[coordonnees[1]+y][coordonnees[0]+x] != "-":
                        test = False
        return test

    def convertCoordonnees(self, coordonnees: str) -> tuple:
        """Convertit les coordonnées du type "C4" en coordonnées du type (3, 4)"""
        letter = coordonnees[0]
        number = coordonnees[1]
        letter = ord(letter) - 65
        return (int(letter), int(number)-1)

    def sunk(self, coordonnees):
        """Vérifie si un bateau est touché"""
        if self.grid[coordonnees[1]][coordonnees[0]] == "-":
            self.grid[coordonnees[1]][coordonnees[0]] = "*"
            return False
        else:
            self.grid[coordonnees[1]][coordonnees[0]] = "@"
            return True