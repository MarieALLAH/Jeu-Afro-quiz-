# Jeux de Quiz sur la Culture Noire :
# Développez un jeu de quiz interactif qui teste les connaissances des utilisateurs sur la culture noire, l'histoire africaine et la musique afro.

# Etape 1
# Créer une grande liste, dans laquelle il y a 3 dictionnaires appelés "questions".
# Pour chaque dictionnaire (question) dans la liste, il y a trois paires clé-valeur :
# 'question': Cette clé contient le texte de la question.
# 'options': Cette clé contient une liste des options de réponse possibles à la question.
# 'correct_answer': Cette clé contient la réponse correcte à la question.

questions = [
    {
        'question': "Quelle danse traditionnelle originaire du Brésil est associée à la culture afro-brésilienne?",
        'options': ["Samba", "Tango", "Flamenco", "Cha-Cha-Cha"],
        'correct_answer': "Samba"
    },
    {
        'question': "Quel est le nom du mouvement artistique et culturel qui a émergé dans les années 1920 à Harlem, New York, mettant en avant la culture noire?",
        'options': ["Cubisme", "Renaissance Harlem", "Impressionnisme", "Surréalisme"],
        'correct_answer': "Renaissance Harlem"
    },
    {
        'question': "Qui est la légendaire chanteuse de soul surnommée 'Queen of Soul'?",
        'options': ["Ella Fitzgerald", "Diana Ross", "Aretha Franklin", "Whitney Houston"],
        'correct_answer': "Aretha Franklin"
    }
]

# Etape 2 : Dans la deuxième étape, afficher le texte de la question, suivi de toutes ses options de réponse à l'utilisateur.

# Définition de la fonction afficher_question
def afficher_question(question):
    print(f"Question: {question['question']}")  # Cette ligne utilise une f-string pour afficher le texte de la question à l'utilisateur. La clé 'question' dans le dictionnaire question contient le texte de la question.
    afficher_reponses(question['options'])  # Cette ligne appelle la fonction afficher_reponses(options) avec les options de réponse de la question actuelle. Cela affiche ensuite toutes les options de réponse à la question.

# Cette fonction affiche chaque option de réponse avec son numéro à l'utilisateur.
def afficher_reponses(options):
    for i, option in enumerate(options, 1):  # Cette ligne parcourt chaque option dans la liste options, en attribuant un numéro i à chaque option, en commençant par 1.
        print(f"{i}. {option}")  # Cette ligne affiche chaque option avec son numéro correspondant à l'utilisateur.

# Parcourt chaque question dans la liste questions et appelle la fonction afficher_question(question) pour afficher chaque question avec ses options de réponse à l'utilisateur.
for question in questions:  # Cette ligne crée une boucle for qui parcourt chaque élément (dictionnaire représentant une question) dans la liste questions.
    afficher_question(question)  # Cette ligne appelle la fonction afficher_question pour chaque question dans la liste questions. Cela affiche le texte de chaque question avec ses options de réponse à l'utilisateur.

# Etape 3 : Gestion des réponses
def gerer_reponse(question):
    reponse_utilisateur = input("Entrez le numéro de votre réponse : ")  # Saisie utilisateur

    if reponse_utilisateur.isdigit():  # Vérifie si la saisie est un nombre
        choix_utilisateur = int(reponse_utilisateur) - 1  # Convertit la saisie en indice de liste
        if 0 <= choix_utilisateur < len(question['options']):  # Vérifie si l'indice est valide
            if question['options'][choix_utilisateur] == question['correct_answer']:  # Vérification
                print("Bonne réponse!")
                return True  # Réponse correcte
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {question['correct_answer']}")
                return False  # Réponse incorrecte
        else:
            print("Numéro de réponse invalide.")
            return False  # Indice invalide
    else:
        print("Veuillez entrer un nombre.")
        return False  # Saisie non numérique

# Etape 4 : Comptage des points
score = 0  # Initialisation du score

# Etape 5 : Boucle du quiz
for question in questions:
    afficher_question(question)
    if gerer_reponse(question):
        score += 1  # Incrémentation du score pour chaque bonne réponse

# Etape 6 : Fin du jeu
print(f"Votre score final est : {score}/{len(questions)}")  # Affichage des résultats

# Encouragement ou correction finale
if score == len(questions):
    print("Félicitations! Vous avez répondu correctement à toutes les questions.")
else:
    print("Merci d'avoir joué! Continuez à apprendre et à explorer la culture noire.")

import tkinter as tk

# Fonction pour afficher les résultats dans une fenêtre graphique
def afficher_resultats(score, total_questions):
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Résultats du Quiz")

    # Couleur de fond
    fenetre.configure(bg="#6495ED")  # Utilisation de la couleur bleue pour le fond

    # Création du tableau pour afficher les scores
    tableau_scores = tk.Frame(fenetre, bg="#6495ED")  # Utilisation de la même couleur pour le fond du tableau
    tableau_scores.pack(pady=20)  # Espacement autour du tableau

    # Étiquette pour le titre du tableau
    etiquette_titre = tk.Label(tableau_scores, text="Scores", font=("Helvetica", 16, "bold"), bg="#6495ED", fg="white")  # Police en gras et couleur de police blanche
    etiquette_titre.grid(row=0, column=0, columnspan=2, pady=10)  # Placement de l'étiquette dans le tableau

    # Étiquette pour afficher le score
    etiquette_score_titre = tk.Label(tableau_scores, text="Score final :", font=("Helvetica", 12), bg="#6495ED", fg="white")
    etiquette_score_titre.grid(row=1, column=0, padx=10, pady=5)  # Placement de l'étiquette dans le tableau

    etiquette_score = tk.Label(tableau_scores, text=f"{score}/{total_questions}", font=("Helvetica", 12), bg="#6495ED", fg="white")
    etiquette_score.grid(row=1, column=1, padx=10, pady=5)  # Placement de l'étiquette dans le tableau

    # Étiquette pour les encouragements ou corrections
    if score == total_questions:
        message = "Félicitations! Vous avez répondu correctement à toutes les questions."
    else:
        message = "Merci d'avoir joué! Continuez à apprendre et à explorer la culture noire."
    
    etiquette_message = tk.Label(fenetre, text=message, font=("Helvetica", 12), bg="#6495ED", fg="white")  # Utilisation de la même couleur pour le fond et la police
    etiquette_message.pack(pady=20)  # Espacement autour du message

    # Bouton pour fermer la fenêtre
    bouton_quitter = tk.Button(fenetre, text="Fermer", command=fenetre.quit, font=("Helvetica", 12))
    bouton_quitter.pack(pady=10)  # Espacement sous le bouton

    # Lancement de la boucle principale
    fenetre.mainloop()

# Appel de la fonction afficher_resultats avec le score et le nombre total de questions
score = 2  # Exemple de score
total_questions = 3  # Exemple de nombre total de questions
afficher_resultats(score, total_questions)