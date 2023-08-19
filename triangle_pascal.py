def main():
    n = int(input("Entrer le nombre de ligne à afficher du tableau de Pascal: "))
    array = array_triangle_pascal(n)
    

def array_triangle_pascal(n):
    array : list = []
    for y in range(n):
        line: list = [1]
        for x in range(y):
            print(x)
            try :
                if x-1 or y-1 >= 0:
                    line.append(array[x-1][y-1] + array[x][y-1])
                else:
                    line.append(1)
            except IndexError:
                line.append(1)
            
        print(array)
        array.append(line)
    return array

def display(array):
    for list in array:
        for element in list:
            print(element, end=" ")
        print()

if __name__ == "__main__":
    main()