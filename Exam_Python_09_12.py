from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


mot1=["c","i","t","r","o","n"] 
proposition = (input("Choisir votre mot (6 lettres)"))

def compare_mot (mot1,proposition):
    for i in range (len(proposition)):
        if proposition[i] == mot1[i]:
            print(Back.RED + proposition[i])
        else:
            print(Back.YELLOW + proposition[i],)
    
        


compare_mot(mot1,proposition)





   

input()