from colored import Style, Fore, Back
import ships
from game import Grid
import bin
import time

def main():

    """Variables"""
    blow : int = 0
    sunk_ships : int = 0
    object_list : list = [ships.A]

    """Lancement du jeu"""
    print("Bonjour !")
    time.sleep(1)
    print("Bienvenue dans le jeu de la bataille navale !")
    time.sleep(1)
    print("Voulez-vous charger une partie ?")
    time.sleep(1)
    print("1. Oui")
    print("2. Non")
    choice = input("Votre choix : ")
    time.sleep(1)

    if choice == "1":
        print("Quel est le nom de la partie à charger ?")

        game_name = input("Nom de la partie : ")
    else :
        print("Voulez-vous placer vos bateaux manuellement ?")
        print("1. Oui")
        print("2. Non")
        choice = input("Votre choix : ")
        time.sleep(1)

        if choice == "1":
            print("Veuillez placer vos bateaux manuellement")
            grid = Grid()
            grid.create()
            ships_place = 0
            while ships_place <= 9:
                print("P Porte-avion C Croiseur T Torpilleur S Sous-marin")
                ship_choice = input("Votre choix : ")
                coordonnees_choice = input("Coordonnées de votre navire : ")
                orientation_choice = input("Orientation de votre navire (marquez 'H' ou 'V'): ")
                if orientation_choice == "H":
                    if grid.testPlaceHorizontal(ship_choice, grid.convertCoordonnees(coordonnees_choice)) == True:
                        ships_place += 1
                        grid.placeShipHorizontal(ship_choice, grid.convertCoordonnees(coordonnees_choice))
                        grid.display()
                    else:
                        print("Impossible de placer le navire ici")
                else:
                    if grid.testPlaceVertical(ship_choice, grid.convertCoordonnees(coordonnees_choice)) == True:
                        ships_place += 1
                        grid.placeShipVertical(ship_choice, grid.convertCoordonnees(coordonnees_choice))
                        grid.display()
                    else:
                        print("Impossible de placer le navire ici")
            print("Tous les navires sont placés")

        else:
            print("L'ordinateur va placer vos bateaux")
            time.sleep(1)
    print("Voici votre grille")
    grid.display()
    print("La partie commence !")

    """Coeur de la partie"""
    while sunk_ships <= 19:
        coordonnees = grid.getCoordonnees()
        if grid.sunk(grid.convertCoordonnees(coordonnees)):
             sunk_ships += 1
        grid.display()
        blow += 1
        print("Nombre de coups : ", blow)
        
    print(f"Bravo, vous avez gagné au bout de {blow} coups!")

main()
"""Prochaine fois dev la partie random,la sauvegarde ainsi que la partie réseau"""
    
        
            
