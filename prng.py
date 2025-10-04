"""
Implémentation de PRNG
Elyas Sahnoune

Il s'agit d'un PRNG qui utilise les racines primitives dans un MCG pour
générer une distribution aléatoire et uniforme. Il y a une fonction pour
générer un entier et une autre pour permuter une liste.
"""
import math, random

random.seed()

# variables privées pour qu'elles ne soient pas accédées par un tiers si jamais
# Trouver une manière de générer la graine autre que la librairie random
__graine: int = random.randint(1, int(1e9 + 6))
__last: int = __graine
__p1: int = 13
__p2: int = 5
__m: int = int(1e9) + 7

def generer_nombre(a: int, b: int) -> int:
    """
    Fonction qui génère un nombre aléatoire en utilisant un generateur 
    de congruence linéaire (LCG). L'implémentation est un générateur 
    multiplicatif (MCG), qui utilise les racines primitives pour créer
    une période de 1e9 + 7
    """

    global __last

    assert(b >= a)
    
    if __last == 0: __last = 1
    
    __last = (__p1 * __last) % __m
    digest: int = (__p2 * __last + 7) % __m 

    return (digest % (b-a+1)) + a 

def generer_permutation(entree:list) -> list:
    """
    Fonction qui prend une liste mutable d'éléments et qui retourne une liste
    contenant les mêmes éléments que le paramètre mais pas nécéssairement dans
    le même ordre
    """
    
    num: int = 0 # indice générée
    l: int = len(entree) # numéros d'éléments à distribuer
    vst: list[bool] = [True]*l # si l'élément a été distribué
    res: list = [] # résultat

    # tant qu'il y a des éléments à distribuer
    while l > 0:
        
        num = generer_nombre(0, len(entree) - 1) # générer indice
        
        # si élément distribué, ressayer, sinon distribuer élément
        if vst[num]:
            res.append(entree[num])
            vst[num] = False
            l -= 1
    
    return res

def test(x: int) -> bool | float:
    
    """
    Fonction qui teste, pour une séquence de x éléments s'ils furent assez bien
    distribués. Si la distribution n'est pas assez uniforme (σ(X) > 2%), elle 
    retourne faux, sinon elle retourne l'écart type résultant
    """

    cmp: list[int] = [0]*10 # le compte des nombres générés par le prng
	
    for i in range(x): 
    
        gnum: int = generer_nombre(0, 9) # nombre généré
		
        if gnum < 0 or gnum > 9: return False
        cmp[gnum] += 1
    
    moy: float = sum(cmp)/len(cmp) # moyenne
    var: float = (sum([v**2 for v in cmp])/len(cmp)) - moy**2 # variance
    et: float = math.sqrt(var) # écart-type
    
    if ((et*10)/x) > 0.02: return False
    return et

def is_correct(x: int = int(1e5), itr: int = 10) -> bool:
    
    """
    Fonction qui teste itr instances différentes du PRNG générant une séquence 
    de x éléments. Si le PRNG échoue dans une des instances, ou bien que le PRNG
    donne deux séquences identiques (ce qui est statistiquement impossible pour 
    itr petit), la fonction retourne faux, sinon elle retourne vrai.
    """
    
    scount: int = itr # nombre de graines à vérifier 
    ln: int = x # longueur de suite
    st: list[float] = [] # ensemble contenant les écart-types déja vus (statistiquement impossible d'avoir deux écart types égaux)
    
    for i in range(1, scount+1): 
    
        rst: float = test(ln)
        if not rst or rst in st: return False
        st.append(rst)
    
    return True
