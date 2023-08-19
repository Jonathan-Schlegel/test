nom_fichier = input("Quel fichier souhtaitez vous lire ?")

try:
    
    nombre = int(input("Combien de fois doit-on imprimer le fichier ? "))
    print(f"Le fichier {nom_fichier} va être imprimé {nombre} fois.")

    with open(nom_fichier) as fp:
        lines = fp.readlines()
        for n in range(nombre):
            for line in lines:
                print(line.strip())
except ValueError:
    print("Désolé, le nombre de fois doit être un entier !")
except Exception:
    print("Désolé le fichier en qustions n'existe pas ! ")
else:
    print("Touts s'est bien passé !")
