from math import sqrt

#### Fonction secondaire


def isprime(p:int)->bool:
    """Indique si le nombre choisie est un nombre premier.
    Args:
        p : nombre entier.
    Returns :
        bool.
    """
    if p < 2: #les nombre <2 ne sont pas premiers
        return False
    for i in range (2,p):
        if p % i ==0:
            return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(2,100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
