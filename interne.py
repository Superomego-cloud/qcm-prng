"""
Base de donnée interne du QCM
Yvan Van de Steene
"""

from qcm, prng_it import *

# réfère toi au fichier exemple.py pour voir comment les données sont 
# traités par le questionnaire

# cette variable est à remplir, elle est la base de données
# Les variables définies ici peuvent être utilisés par les fonctions
# mets deux tirets bas au début du nom de ton variable pour qu'elle ne
# soit pas accessible à l'éxterieur du fichier
__database : list


def initialiser_donnees(entree: str) -> None:
    """
    Cette fonction prend le nom du fichier et initialise les données du 
    questionnaire, destinéees à l'utilisation des autres fonctions
    """

def traiter_question(entree: str) -> tuple[bool, str]:
    """
    Cette fonction sera appelée par l'élément d'affichage pour savoir si la 
    réponse donnée est correcte ou fausse
    """

def question_suivante() -> list:
    """
    Cette fonction sera appelée par l'élément d'affichage pour prendre les 
    données de la question suivante. S'il n'y a plus de questions, elle donne 
    une liste vide.
    """

def note_finale() -> tuple[int | None, int | None]:
    """
    Cette fonction sera appelée par l'élément d'affichage dès que le 
    questionnaire est terminé pour donner la note finale avec les deux systèmes
    de notation. La première valeur est la notation normale, la deuxième est 
    la notation sévère. Si les paramètres de l'utilisateur font qu'il veuille 
    qu'un des deux, l'autre valeur doit être None
    """
