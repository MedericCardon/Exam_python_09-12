import random



from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


mot1=["c","i","t","r","o","n"]
mot2=["t","o","m","a","t","e"]
mot3=["c","i","t","r","o","n"]
mot4=["c","i","t","r","o","n"]
mot5=["c","i","t","r","o","n"]
mot6=["c","i","t","r","o","n"]
mot7=["c","i","t","r","o","n"]
mot8=["c","i","t","r","o","n"]
mot9=["c","i","t","r","o","n"]
mot10=["c","i","t","r","o","n"]


proposition = random.(1,2,3,4,5,6,7,8,9,10)
print(proposition)

def compare_mot (mot1,proposition):
    for i in range (len(proposition)):
        if proposition[i] == mot1[i]:
            print(Back.RED + proposition[i], end="")
            print("félicitation vous avez gagné !")
        if proposition[i] != mot1[i]:
            print(Back.YELLOW + proposition[i], end="")
      
    

    






   

input()