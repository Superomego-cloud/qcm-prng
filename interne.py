"""
Base de donnée interne du QCM
Yvan Van de Steene
"""

from qcm import *
from prng import *

# réfère toi au fichier exemple.py pour voir comment les données sont 
# traités par le questionnaire

# cette variable est à remplir, elle est la base de données
# Les variables définies ici peuvent être utilisés par les fonctions
# mets deux tirets bas au début du nom de ton variable pour qu'elle ne
# soit pas accessible à l'éxterieur du fichier
__database : list
__last : int = 0
__malus : int = 0
__bonne : int = 0
__mode : list[bool, bool] = [True]*2

def initialiser_modes(entree: str) -> None:
    """
    Fonction qui permet de définir le mode de notation par la suite.
    Elle prend comme entrée les différentes options qu'a l'utilisateur.
    N: notation normale, M: notation sévère, D: les deux styles  
    Le mode D est celui par défaut.
    """
    ins = entree.strip()
    if ins.upper() == "N": __mode[1] = False
    elif ins.upper() == "M": __mode[0] = False


def initialiser_donnees(entree: str) -> None:
    """
    Cette fonction prend le nom du fichier et initialise les données du 
    questionnaire, destinéees à l'utilisation des autres fonctions
    """
    global __database 


    __database = build_questionnaire(entree) 
    __database = generer_permutation(__database)

def traiter_question(entree: str) -> tuple[bool, str]:
    """
    Cette fonction sera appelée par l'élément d'affichage pour savoir si la 
    réponse donnée est correcte ou fausse
    """
    
    ret = [True, ""]

    entree = int(entree)
    if __database[__last][1][entree][1]: 
        __bonne += 1
        ret[0] = True
    else: 
        __malus += 1
        ret[0] = False

    ret[1] = __database[__last][1][entree][2]

    return tuple(ret)
         
 
def question_suivante() -> list:
    """
    Cette fonction sera appelée par l'élément d'affichage pour prendre les 
    données de la question suivante. S'il n'y a plus de questions, elle donne 
    une liste vide.
    """

    __database[__last][1] = generer_permutation(__database[__last][1])
    __last += 1

    if __last > len(__database):
        return []

    return __database[__last - 1]


def note_finale() -> tuple[int | None, int | None]:
    """
    Cette fonction sera appelée par l'élément d'affichage dès que le 
    questionnaire est terminé pour donner la note finale avec les deux systèmes
    de notation. La première valeur est la notation normale, la deuxième est 
    la notation sévère. Si les paramètres de l'utilisateur font qu'il veuille 
    qu'un des deux, l'autre valeur doit être None
    """
    return ((__bonne if __mode[0] else None),(__bonne - __malus if __mode[0] else None))
