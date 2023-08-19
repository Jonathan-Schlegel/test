def anagramme(word1 : str, word2 : str) -> bool:
    test : bool = True
    for letter in word1:
        if letter not in word2 or len(word1) != len(word2):
            test : bool = False
            break
    return test



if anagramme("voile", "olive"):
    print("C'est un anagramme")
else:
    print("Ce n'est pas un anagramme")