

from turtle import *
import random
from tkinter import * # Tkinter pour les bouttons
import time

reset()

# Le code de jeu

gagne = 0 # Variable pour les parties gagnées
perdu = 0 # Variable pour les parties perdues
lettres = 0 # Variable pour les lettres trouvées

def jeu(dif, couleur, lettres, gagne, perdu):
  
  timer = [60, 45, 30, 15, 10, 5] # Stocke les temps temps "repères" ( 60s, 30s etc...)

  lim = 180 # Temps maximum
  
  mot = random.choice(dif)
    
  def texte_supprimable(tortue, mot, font): # Pour effacer du texte ( cf powerpoint pour voir le résonnement ) 
    texte = Turtle() # Création d'une nouvelle tortue
    texte.hideturtle()
    texte.up()
    texte.goto(tortue.pos()) # Déplacer la nouvelle tortue à l'emplacement de l'ancienne
    texte.down()
    texte.write(mot, font=font) # Ecrire ce qu'on veut avec le font souhaité
    return texte

  def rejouer(dif, couleur, lettres, gagne, perdu): # Fonction qui va demander au joueur si il veut rejouer
      Screen().bgcolor(couleur)
      reponse = textinput("Voulez vous rejouer ?", "\n repondez oui/non").upper()
      if reponse == "NON":
          localisation((0, -12))
          color('black')
          score(perdu, gagne, lettres) # Le joueur va voir son score si il répond par non
          time.sleep(10)
          bye() # Pour fermer la fenêtre turtle quand le joueur a fini
      else:
          jeu(dif, couleur, lettres, gagne, perdu) # Si le joueur met quelque chose d'autre que non ( oui ), il va rejouer en lancant la fonction jeu.

  def localisation(coord): # Pour déplacer la tortue
      up()
      goto(coord)
      down()      
  
  def ecriture_1(lettre, mot, coordonne, font, vrai, longeur): # vrai = liste où les lettres trouvées seront stockées
      localisation((coordonne[mot.index(lettre)] - (longeur / 2), 10)) # On va aller AU CENTRE du tiret
      write(lettre, font = font) #Ecrire la lettre
      vrai.append(lettre)
      
  def ecriture_2(lettre, mot, indexe, marge_derreur, coordonne, font, vrai, rep, longeur): # Quand le mot contient deux ou plusieurs fois la même lettre.
       for z in range(rep): # Le rep c'est le nombre de répétitions d'une lettre x dans un mot. Par exemple, rep de s dans "assassin" vaudra 4
            indexe.append(mot.index(lettre)) # Indexe est une liste qui stocke l'indice de la première apparation de la lettre x ( c'est ce que fait la commande index())
            mot.remove(lettre) # On supprime la première fois où apparait cette lettre pour avoir toutes les coordonnées des lettres et donc éviter des erreurs ( des lettres qui s'écrivent sur d'autres par exemple )
       # Après ce processus, assassin deviendra aasin ( on enlève toutes les répétions d'une lettre x pour n'en garder qu'une seule)
       for a in indexe:
            localisation((coordonne[a] + marge_derreur - (longeur / 2), 10))
            marge_derreur += 2 * longeur # C'est pour éviter une erreur. Sans cette variable, l'ordinateur va en effet une lettre sur l'autre
            write(lettre, font = font)
            vrai.append(lettre)
  
  
  def game_perdu(mot, couleur): # Quand le joueur perd, cette fonction va lui afficher le mot qu'il avait
      Screen()
      Screen().bgcolor(couleur)
      up()
      goto(-125, 200)
      write(f"Votre mot était: {mot}", font = style_notif)
      
  def score(perdu, gagne, lettre_trouves): # Cette fonction va afficher au joueur ses stats. A savoir: le nombre de parties gagnées, perdues et le nombre de lettres trouvées
        y = 100
        for i in [perdu, gagne, lettre_trouves]:
            y -= 100
            localisation((-125,y))
            if y == 0:
                write(f" Vous avez perdu {i} parties", font = style_notif, align = 'left') # des f ( formatting) strings
            elif y == - 100:
                write(f" Vous avez gagne {i} parties", font = style_notif, align = 'left')
            else:
                write(f" Vous avez trouvé {i} lettres", font = style_notif, align = 'left')
      
  tortue = Turtle()
  tortue.hideturtle()
  mot = mot.upper()  
  
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  message_trouve = ["Bravo!", " Bien Trouvé ", " Très bien"]

  message_n = ["Essayez encore une fois", " Pas la bonne lettre", "Faux","retentez"]

  message_w = ["Congratulations", "vous avez gagne!", " Impréssionant", " Bien Joué"]

  message_l = ["Dommage :(", "Perdu!","Next time :("]
  Screen()
  speed(1000)
  positions_x = []
  Screen().screensize(1400, 800, couleur)
  
  tortue.up()
  tortue.goto(-400,0)
  tortue.down()
  for i in [3,2,1]: # compte à rebours avant le début de la partie (3s)
      a = texte_supprimable(tortue, f"La partie commence dans \n {i}....", font = ('Courier', 50, 'bold' ))
      time.sleep(1)
      a.clear()
  Screen().clear()
  Screen().bgcolor(couleur)
      
  longeur = 850 / (len(mot) * 2) # 850 pixels est la longeur que va occuper le mot et on veut que ça soit proportionnel
  localisation((-350, 0))
  for i in range(len(mot)):
      width(4)
      down()
      forward(longeur)
      positions_x.append(xcor()) # On va stocker tous les coordonnées d'abscisse des tirets dans cette liste positions_x
      up()
      forward(longeur)
  
  style_notif = ('Courier', 25, 'italic')
  style_w = ('Courier', int(longeur/ 1.5), 'italic') # On veut que les lettres soit proportionnelles aux tirets
  style_mot = ('Courier', int(longeur / 2), 'bold')
  style_messagefin = ('Courier', 50, ' italic ')
  erreurs = 0
  vrai = [] # Stocker les lettres trouvées
  liste = [] # Pour stocker toutes les lettres utilisées et éviter les répétitions
  liste_affiche = [] # Pour afficher les lettres utilisées
  
  
  for s in [-1, 0]: # Pour afficher les premières et dernieres lettres
    rep = mot.count(mot[s]) # Pour compter combien de fois la première ou la dernière lettre apparaît dans le mot
    if rep == 1:
        ecriture_1(mot[s], mot, positions_x, style_mot, vrai, longeur)
        list(mot).pop(s) # Supprimer la lettre pour qu'à la fin, len de liste vrai soit égale à len de mot
        liste_affiche.append(f'{mot[s]} ,') # C'est pour l'affichage des lettres utilisées sur turtle
        liste.append(mot[s])
    else:
        indexe = []
        marge = 0
        ecriture_2(mot[s], list(mot), indexe, marge, positions_x, style_mot, vrai, rep, longeur)
        liste_affiche.append(f'{mot[s]} ,')
        liste.append(mot[s])
    
  while erreurs < 8 or len(mot) == len(vrai): # On stoppe le jeu quand l'utilisateur a gagné ( En trouvant toutes les lettres ( len vrai = len mot ) ou perdu ( en faisant un nb d'erreurs = 8)
    debut = time.perf_counter() # Le début du compte à rebours
    color('black')
    tortue.up()
    tortue.goto(- 500, - 200)
    liste1 = texte_supprimable(tortue, f'Les lettres que vous avez déjà utilisé: \n {"".join(liste_affiche)}', font = style_notif)
    proposition = textinput("Vos reponses", "Saisissez une lettre: ").upper() # On Demande à l'utilisateur, via une fenêtre turtle, de donner une lettre. Cette dernière sera mise en majiscule et stockée dans proposition
    rep = mot.count(proposition) # Pour compter combien de fois proposition est dans le mot
    if proposition not in alphabet: # Au cas où le joueur aurait donné un caractère qui n'est pas présent dans la liste alphabet
        tortue.up()
        tortue.goto(0, - 200)
        tortue.down()
        mot1_affiche = texte_supprimable(tortue, "Vous ne pouvez pas utiliser ce caractère", font = style_notif)
        time.sleep(1.5)
        mot1_affiche.clear() # Suppression du mot1_affiche après une seconde
        time.sleep(1) # Il ne sera pas pénalisé et aura un message lui disant qu'il ne peut pas utiliser cette lettre
    elif proposition in liste or proposition in vrai: # Si le joueur a écrit la même lettre à deux reprises
        tortue.up()
        tortue.goto(0, - 300)
        tortue.down()
        mot_affiche = texte_supprimable(tortue, "Lettre déjà utilisée", font = style_notif)
        time.sleep(1) 
        mot_affiche.clear() # Il ne sera pas pénalisé et aura un message lui disant qu'il a déjà utilisé cette lettre
    elif rep == 0 and proposition not in liste and proposition in alphabet: # Si proposition n'est ni dans le mot, ni dans la liste qui stocke les lettres utilisées et dans l'alphabet
        erreurs += 1 # Il sera pénalisée
        tortue.up()
        tortue.goto(0,200)
        tortue.down()
        l = texte_supprimable(tortue, random.choice(message_n), font = style_notif) # Affichage d'un message avertissant le joueur qu'il s'est trompé
        if erreurs == 1: # Dessiner au fur et à mesure la barre du pendu en fonction du nombre erreurs du joueur
            localisation(( - 500, 0 ))
            width(4)
            #la barre du sol
            down()
            color("brown")
            left(180)
            fd(100)
            up()
            left(180)
            fd(50)
            down()
            left(90)
            #grande barre
            fd(300)
            coord1 = pos() # On sauvegarde la position du dernier point pour y retourner et dessiner la suite du pendu si l'utilisateur a fait une erreur supplémentaire
        elif erreurs == 2:
            color("brown")
            localisation(coord1) # On va aller aux coordonnées du dernier point ( coord1 )
            right(90)
            #barre petite en haut
            fd(100)
            a2 = pos()
        elif erreurs == 3:
            color("brown")
            localisation(a2)
            width(3)  #corde
            right(90)
            fd(50)
            a3 = pos()
        elif erreurs == 4:
            localisation(a3)
            color("red")  #tête du pendu
            right(90)
            begin_fill()
            circle(20)
            end_fill()
            up()
            left(90)
            fd(40)
            down()
            a4 = pos()
        elif erreurs == 5:
            localisation(a4)
            color("black")  #corps du pendu
            right(360)
            fd(100)
            a8 = pos()
            up()
            left(180)
            fd(80)
            a5 = pos()
        elif erreurs == 6 :
            localisation(a5)
            right(125)  #premier bras
            fd(50)
            up()
            right(180)
            a6 = pos()
        elif erreurs == 7 :
            localisation(a6)
            fd(50)
            down()
            left(75)  #deuxième bras
            fd(50)
            up()
        elif erreurs == 8:
            localisation(a8)
            a9 = pos()
            forward(60)
            left(45) #première jambe
            up()
            localisation(a9)
            right(-45) #deuxième jambe
            fd(60)
        time.sleep(2)
        l.clear()
    elif rep == 1 and proposition not in vrai: # Si proposition est une fois dans le mot et aussi non utilisée ( pas dans vrai )
        ecriture_1(proposition, list(mot), positions_x, style_mot, vrai, longeur) # Appeler la fonction ecriture_1 pour écrire la lettre là où elle devrait être
        tortue.up()
        tortue.goto(0,200)
        tortue.down()
        w = texte_supprimable(tortue, random.choice(message_trouve),style_notif) # On écrit un message qui félicite le joueur
        time.sleep(2)
        w.clear() # On supprime ce message après deux secondes
        lettres += 1 # On ajoute 1 à la variable qui stocke les lettres trouvées 
    elif rep > 1 and proposition not in vrai: # Si la proposition est plusieurs fois dans le mot et non utilisée ( pas dans vrai )
        marge = 0
        indexe = []
        ecriture_2(proposition, list(mot), indexe, marge, positions_x, style_mot, vrai, rep, longeur)
        tortue.up()
        tortue.goto(-350,200)
        tortue.down()
        w = texte_supprimable(tortue, random.choice(message_trouve),style_notif)
        time.sleep(2)
        w.clear()
        lettres += 1
    liste_affiche.append(f'{proposition} ,') # Mise en forme de la liste de lettres qu'on va afficher ( ça va être comme ça: lettre, | au lieu de: [lettre], )
    liste.append(proposition) # Ajout de proposition à la liste de lettres utilisées

    if len(vrai) == len(mot): # Pour voir si le joueur a gagné
        time.sleep(2)
        localisation((-350,200))
        time.sleep(4)
        write(random.choice(message_w), font = style_messagefin)
        time.sleep(4)
        gagne += 1 # Ajout à la variable gagne qui stocke le nombre de parties gagnées +1
        Screen().clear()
        rejouer(dif, couleur, lettres, gagne, perdu) # Fonction qui va demander au joueur si il veut rejouer
        
    if erreurs == 8: # Si le joueur a fait 8 erreurs, il va perdre
        time.sleep(2)
        localisation((-350,200))
        time.sleep(4)
        write(random.choice(message_l), font = style_messagefin) # Affichage d'un mot lui disant qu'il a perdu
        time.sleep(4)
        perdu += 1 # Ajout à la variable perdu qui stocke le nombre de parties perdues +1
        Screen().clear()
        game_perdu(mot, couleur) # Afficher le mot qu'il n'a pas su trouvé
        time.sleep(5)
        rejouer(dif, couleur, lettres, gagne, perdu) # Demander au joueur si il veut rejouer
        
    
    liste1.clear() # Effacer la liste qui affiche les lettres utilisées pour la mettre à jour
    fin = time.perf_counter() # Fin du compte à rebours
    lim -= int((fin - debut)) # Calcul du temps restant en faisant 3 min - le temps écoulé
    for _ in timer:
        if lim <= _ and lim > 0: # Pour voir si le joueur lui reste un temps inférieur ou égal à la première valeur de la liste timer
            timer.pop(0) # On supprime la première valeur en continu pour éviter d'afficher au joueur " il vous reste 60s" à chaque tentative ou afficher "il vous reste 60s" suivie de " il vous reste 45s"
            tortue.up()
            tortue.goto(170, 200)
            aver = texte_supprimable(tortue, f"il vous reste moins de {_} s" ,style_notif) # Avertissement pour le joueur
            time.sleep(2)
            aver.clear()
        elif lim <= 0: # Si le temps restant est inférieur ou égale à 0
            tortue.up() # Afficher le mot quand l'utilisateur a perdu.
            tortue.goto(0, 200)
            write(random.choice(message_l), font = style_messagefin)
            perdu += 1
            sleep(3)
            Screen().clear()
            game_perdu(mot, couleur)
            time.sleep(5)
            rejouer(dif, couleur, lettres, gagne, perdu)
            break

# Les listes pour les mots

easy = ["Instrument","Sovietique","Patrimoine","Adolescent","Andalousie","Artificiel","Specialite","connexion", "Informatique","Musique"]
medium = ["Absorption","Accommoder","Assurement","Beneficier","Bijouterie","Braconnier","Brouillard", "Assassin","superstition"]
hard = ["Bouddhiste", "Capricorne","Electorale","Energisant","Longuement","Marsupiale","Pseudonyme","Somptueuse","annexion","suspicions"]

# Création des fonctions pour les bouttons

def facile():
    jeu(easy,"#2c75ff",lettres, gagne, perdu)

def moyen():
    jeu(medium,"#ffe436",lettres, gagne, perdu)

def difficile():
    jeu(hard,"#f7230c", lettres, gagne, perdu)

# Choix de la difficulté

root = Tk()  # Création de la fenêtre pour le boutton
root.title("Choix de la difficulté")
root.geometry("600x300")  # Surface de la fenêtre du boutton
root.configure(bg="#0095b6")  # Change la couleur de fond de la fenêtre root
instruction = Label(root, text = "Bienvenue! Le jeu du pendu est un jeu dont le but est de deviner les lettres d'un mot choisi aléatoirement. \n Choisissez d'abord votre difficulté et cliquer sur le boutton Jouer. \n PS: Plus la difficulté est grande, plus les mots sont rares et soutenus. \n Vous avez 3min pour trouver le mot. \n Bonne Chance!", bg="#0095b6", fg="#FFFFFF").place(x = 10 ,y =  200)

# Création des bouttons qui seront dans la fenêtre root et executeront ce qu'il y a dans la fonction facile, moyen ou difficile.

boutton = Button(root, text="facile", bg="#0095b6", fg="#FFFFFF", padx=50)
boutton.config(command=facile)
boutton.pack(side=LEFT)
boutton1 = Button(root, text="Moyen", bg="#0095b6", fg="#FFFFFF", padx=50)
boutton1.config(command=moyen)
boutton1.pack(side=LEFT)
boutton2 = Button(root, text="difficile", bg="#0095b6", fg="#FFFFFF", padx=50)
boutton2.pack(side=LEFT)
boutton2.config(command=difficile)
close_b = Button(root,text="Jouer",bg="#0095b6", fg="#FFFFFF",padx=100, command=root.destroy).pack(side=LEFT) # Pour fermer la fenêtre de la difficulté


mainloop()

