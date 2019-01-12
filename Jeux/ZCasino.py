import os
from random import randrange
from math import ceil

print("Vous vous installez à la table de roulette")

mise = input("Mise d'un nombre entre 0 et 49:")

try:
  mise = int(mise)
  assert mise >= 0
  assert mise <= 49
  
except:
  print("Le nombre inscrit n'est pas un bombre entre 0 et 49")
  mise = input("Mise d'un nombre entre 0 et 49:")
    
print("Vous misez sur le chiffre", mise)

if mise%2 == 0:
  pair = True
  print("Votre chiffre de mise est pair")
  
else:
  impair = True
  print("Votre chiffre de mise est impair")
  
      
argent = input("Mise d'une somme d'argent égal ou inférieur à 1000$:")
  
try:
  argent = int(argent)
  assert argent > 0
  assert argent <= 1000
  
except:
  print("La somme d'argent misée n'est pas valide")
  argent = input("Mise d'une somme d'argent égal ou inférieur à 1000$:")
  
print("Vous misez", argent, "$")
  

  
  
print("Le croupier va lancer la roulette")

miseordi = randrange(50)

print("Le croupier a tiré le chiffre", miseordi)


if miseordi == mise:
  print("Vous avez gagner")
  argent = argent*3
  argent = ceil(argent)
  print("Vous gagnez la somme de", argent, "$")
 

  
elif miseordi != mise:

  
  if miseordi%2==0 and mise%2 == 0 :
    argent = argent / 2
    argent = ceil(argent)
    print("Le chiffre du croupier et votre chiffre sont de la même couleur, vous êtes rembourser de 50% de la somme misée.")
    print("Vous êtes rembourser de", argent)
	
  elif miseordi%2 != 0 and mise%2 != 0:
    argent = argent / 2
    argent = ceil(argent)
    print("Le chiffre du croupier et votre chiffre sont de la même couleur, vous êtes rembourser de 50% de la somme misée.")
    print("Vous êtes rembourser de", argent)
    
  
  else:
    print("Vous avez perdu, vous ne touchez rien et vous n'êtes remboursé de rien")


os.system("pause")