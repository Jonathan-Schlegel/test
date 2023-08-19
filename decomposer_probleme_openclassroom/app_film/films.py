from abc import ABC
"""
class film(ABC):

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def genre(self):
        pass
    
    def __str__(self):
        return f"{self.title} {self.year}"
"""
class filmDVD():

    def __init__(self, title, year):
        self.title = title
        self.year = year
    
    def __str__(self):
        return f"{self.title} {self.year}"

    def genre(self):
        return "DVD"
    
class filmVHS():

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} {self.year}"
    
    def genre(self):
        return "VHS"

