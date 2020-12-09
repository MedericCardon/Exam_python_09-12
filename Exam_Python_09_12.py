import random



from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


mot1=["c","i","t","r","o","n"]
mot2=["t","o","m","a","t","e"]
mot3=["b","i","t","r","o","n"]
mot4=["h","i","t","r","o","n"]
mot5=["i","i","t","r","o","n"]
mot6=["j","i","t","r","o","n"]
mot7=["k","i","t","r","o","n"]
mot8=["l","i","t","r","o","n"]
mot9=["m","i","t","r","o","n"]
mot10=["n","i","t","r","o","n"]

mot=""
proposition=""



mot=random.randint(1,10)
if (mot==1):
    mot=mot1
if (mot == 2):
    mot=mot2
if (mot == 3):
    mot=mot3
if (mot == 4):
    mot=mot4
if (mot == 5):
    mot=mot5
if (mot == 6):
    mot=mot6
if (mot == 7):
    mot=mot7
if (mot == 8):
    mot=mot8
if (mot == 9):
    mot=mot9
if (mot == 10):
    mot=mot10
  

def compare_mot (mot, proposition):
    proposition = input("Votre proposition ? (6 lettres) : ")
    for i in range (len(proposition)):
        if proposition[i] == mo[i]:
            print(Back.RED + proposition[i], end="")
            print("félicitation vous avez gagné !")
        if proposition[i] != mot[i]:
            print(Back.YELLOW + proposition[i], end="")
      
    

    

print(mot)



   

input()