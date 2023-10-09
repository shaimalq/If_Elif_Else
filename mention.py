n1=int(input("saisir 1 ere note :"))
n2=int(input("saisir 2 eme note :"))
n3=int(input("saisir 3 eme note :"))
m=(n1+n2+n3)/3
if m<10:
    mention="insuffisant"
elif m>=10 and m<12:
    mention="passable"
elif m<=12 and m<14:
    mention="assez bien"
elif m>=14 and m<16:
    mention="bien"
else:
    mention="trés bien"
print("la moyenne de l'etudiant est:",m)
print("la mention de l'etudiant est :",mention)