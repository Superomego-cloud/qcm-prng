import qcm

"""
    Exemple d'utilisation de la librairie de lecture de fichiers QCM
"""

def traiter_entree(qst, )

if __name__ == '__main__':
    filename = "QCM.txt"

    ans = [0, 0]
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    
    print("Le questionnaire est une liste de questions.")
    
    # q[0] est la question, q[1] la liste de réponses (i l'indice de la question)
    for i, q in enumerate(questions): 
        
        print(f"\tQuestion {i+1}: {q[0]}")
       
        # Le j est l'indice
        for j, r in enumerate(q[1]):  
            print(f"\t\tReponse {str(j+1)}:")
            print("\t\t\tMessage: \"" + r[0] + "\"")
            print("\t\t\tCorrect: " + str(r[1]))
            print("\t\t\tFeedback: \"" + r[2] + "\"")

