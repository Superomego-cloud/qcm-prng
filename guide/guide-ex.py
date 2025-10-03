"""
Fichier exemple
Elyas Sahnoune, 3 Octobre 2025

Il s'agit d'un fichier contenant un ensemble de snippets de code explicitant les conventions 
et les idées présentées dans le fichier annexe guide.txt
"""

# Annotations de variables simples
x: int = 1 # ceci est un entier
pq: float = 0.5 # ceci est un décimal
is_true: bool = True # ceci est une valeur booléene
magritte: str = "Ceci n'est pas une pipe" # ceci est une chaine de charactères

y: int | None = None # Le type est soit int soit rien
y = 3 # ne pas annoter après la declaration de la variable

v : None # il n'est pas nécessaire de donner une valeur pour annoter une variable, les annotations ne sont pas vérifiés
# v : int # Ne REANNOTEZ PAS deux fois une variable. Cette ligne est en commentaire pour dire qu'elle est fausse

# annotations des conteneurs
jour: list = [3.07, 3, "Octobre", 2008, True] # une liste quelconque
chiffres_de_pi: tuple[int] = (3, 1, 4, 1) # une tuple d'entiers
sont_premiers: tuple[list[int], bool] = ([2, 3, 5, 7], True) # un tuple de deux éléments (il y a une liste dans une liste)

# annotations de fonctions
def multiplier(x: int, y: int) -> int: ...
def somme(liste: list[int]) -> int: ...
def supersomme(...) -> int: ...
def pivot_en_place(matrice: list[list]) -> None: ...

# exemples de raccoucis
if is_true: x += 1 # conditionnel

while is_true: x += 1 # boucle while

for i in range(x): pq += 1 # boucle for 

def addition(x: int, y: int) -> int: return x + y # fonction

minfunc = lambda x, y : (x if x <= y else y) # fonction anonyme (elle peut être utilisée comme une valeur)

a: int, b: int, c: int = [1, 2, 3] # assignement des valeurs 
a, b = b, a # échange des valeurs (x = 2, y = 1)

chaine_format: str = f"Les chiffres sont {x}, {y} et {z}" # resulte en "Les chiffres sont 2, 1 et 3"

generateur_liste = [i**2 for i in range(1, 10)] # génère une liste des dix premiers carrés (1, 4, 9, ...)

generateur_2 = [i%3 for i in generateur_liste] # le conteneur peut également être une liste/tuple

# exemple de code obéissant aux conventions
""" 
Calculatrice de PGCD
Elyas Sahnoune, 6 Juillet 2069

Il s'agit d'un code qui utilise l'algorithme d'euclide pour calculer en temps logarithmique le plus grand commun diviseur de deux 
nombres fournis par l'utilisateur.
"""

def pgcd(x: int, y: int) -> int:

    """
    Cette fonction utilise la définition récursive fournie par l'algorithme d'euclide pour calculer
    le plus grand commun diviseur des deux nombres x et y
    """

    x, y = min(x, y), max(x, y) # On s'assure que x < y
    reste = y%x 

    # bloc conditionnel condensé qui montre l'intégralité de l'algorithme
    if reste == 0: return x
    else: return pgcd(x, reste)

# version condensée de la fonction anonyme
pgcd_anonyme = lambda a, b: min(a, b) if not max(a, b)%min(a, b) else pgcd_anonyme(min(a, b), max(a,b)%min(a,b)) 

# lecture des variables et conversion en int
x: int, y: int = map(int, (input("x: "), input("y: ")))

# lecture du résultat et conversion en chaine de charactères pour affichage
resultat: int = pgcd(x, y)
representation_char: str = str(resultat)

# affichage du résultat
print(representation_char)
