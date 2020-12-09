from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')




def compare_mot (mot1, proposition):
    if proposition[1] == mot1[1]:
        print(Back.YELLOW + proposition[1])
        






proposition = (input("Choisir votre mot (6 lettres)"))

mot1=["c","i","t","r","o","n"]    

input()