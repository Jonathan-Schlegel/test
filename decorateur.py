user = "joj"

def mon_decorateur(func):

    def refusé():
        print("Accès refusé")
    if user != "jojo":
        return refusé

    return func
            
@mon_decorateur
def ma_fonction(numb1,numb2):
    print(numb1+numb2)

ma_fonction(1,1)