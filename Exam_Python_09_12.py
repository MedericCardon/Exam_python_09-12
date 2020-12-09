from colorama import Fore, Back, Style
print(Fore.WHITE + 'some red text')
print(Back.YELLOW + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


mot1=["c","i","t","r","o","n"]


def mot_desordre (mot1):
    for i in range (len(mot1)):
        print(mot1)

mot_desordre(mot1)
input()