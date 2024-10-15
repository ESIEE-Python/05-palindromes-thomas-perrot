"""
Ce module vérifie si il y a un palindrome dans une chaine de caractères
"""

#### Fonction secondaire
def ispalindrome(p):
    """
    Vérifie si la string donnée est un palindrome

    Args:
        p (String): La chaîne à vérifier.

    Returns:
        bool: True si le String est un palindrome, sinon False.
    """
    accents = str.maketrans(
        "áàâäãåæéèêëíìîïóòôöõøœúùûüçñýÿÁÀÂÄÃÅÆÉÈÊËÍÌÎÏÓÒÔÖÕØŒÚÙÛÜÇÑÝŸç",
        "aaaaaaeeeeeiiiioooooooeuuuucnyAAAAAAEEEEIIIIOOOOOOOEUUUUCNYYc"
    )
    p = p.translate(accents)
    p = ''.join(filter(str.isalnum, p)).lower()
    return p == p[::-1]

#### Fonction principale
def main():
    """
    Appelle la fonction ispalindrome.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
