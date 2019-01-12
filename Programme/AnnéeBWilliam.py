# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non

annee=input("Saisis année:")

annee=int(annee)
if annee%4 !=0:
   print("Année non bissextile")
elif annee%4 == 0 and annee%100==0 :
 if annee%400 == 0:
    print("Année bissextile")
 elif annee%400 !=0:
    print("Année non bissextile")
elif annee%4 == 0 and annee%100!=0 :
   print("Année bissextile")