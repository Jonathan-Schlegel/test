class Clean:

    def get_title(tuple_film):
        return tuple_film[0][:-6].title()
    
    def get_year(tuple_film):
        return tuple_film[0][-5:-1]
    
    def get_support(tuple_film):
        return tuple_film[1].upper()
    
    def get_friend(tuple_friend):   
        return tuple_friend[0]
    
    def get_film_friend(tuple_friend):
        return tuple_friend[1].title()
