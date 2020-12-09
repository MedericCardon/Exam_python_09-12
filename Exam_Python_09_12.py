import random



from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


mot1=["c","i","t","r","o","n"]
mot2=["t","o","m","a","t","e"]
mot3=["a","t","o","u","t","s"]
mot4=["c","i","n","e","m","a"]
mot5=["c","h","o","i","s","i"]
mot6=["l","e","t","t","r","e"]
mot7=["m","a","r","r","o","n"]
mot8=["a","c","t","i","v","e"]
mot9=["m","i","n","u","i","t"]
mot10=["g","i","t","h","u","b"]

mot=""
proposition=""

# Charger un mot aléatoire :

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

print(mot)





def compare_mot (mot, proposition):
    print("")
    proposition = input("Votre proposition ? (6 lettres) : ")
    for i in range (0,1):
        if proposition[0] == mot[0]:
            print(Back.RED + proposition[0], end="")
        if proposition[0] != mot[0]:
            print(Back.BLUE + proposition[0], end="")
      
        if proposition[1] == mot[1]:
            print(Back.RED + proposition[1], end="")
        if proposition[1] != mot[1]:
            print(Back.BLUE + proposition[1], end="")
            
        if proposition[2] == mot[2]:
            print(Back.RED + proposition[2], end="")
        if proposition[2] != mot[2]:
            print(Back.BLUE + proposition[2], end="")
      
        if proposition[3] == mot[3]:
            print(Back.RED + proposition[3], end="")
        if proposition[3] != mot[3]:
            print(Back.BLUE + proposition[3], end="")

        if proposition[4] == mot[4]:
            print(Back.RED + proposition[4], end="")
        if proposition[4] != mot[4]:
            print(Back.BLUE + proposition[4], end="")
      
        if proposition[5] == mot[5]:
            print(Back.RED + proposition[5], end="")
        if proposition[5] != mot[5]:
            print(Back.BLUE + proposition[5], end="")
            
        print(Style.RESET_ALL)
            

def cherche_lettre (mot):
    for i in range (0,1):
        i = mot[2]
        print(i)
    return i    
        

          
cherche_lettre(mot)

compare_mot(mot, proposition)

input()