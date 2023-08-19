class User:
    def __init__(self, firstname, film = ""):
        self.firstname = firstname
        self.film = film

    def add_film(self, title_film):
        self.film = title_film
    
    def del_film(self):
        self.film = ""

    def __str__(self):
        return f"{self.firstname} {self.film}"


