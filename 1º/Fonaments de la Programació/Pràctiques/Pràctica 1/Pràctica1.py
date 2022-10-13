# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
 
import random
#1
def PresentacioJoc():
    print("Pedra, paper, tisores, llangardaix, Spock és un joc d'atzar ampliació del popular Pedra, paper, tisores Creat per Sam Kass amb Karen Bryla http://www.samkass.com/theories/RPSSL.html")
    print("Popularitzat per Sheldon Cooper a la sèrie Big Bang Theory.")
    print("Es fa servir per solucionar una disputa entre Sheldon i Raj en el capítol The Lizard - Spock Expansion")
    print("El joc és al millor de N partides on N és un nombre senar")
    return None


#2

def Senar(num):
    if num == 0:
        senar = False
    if num%2 == 0:
        senar = False
    else:
        senar = True
        
    return senar

#3
    
def LlegirSenar(num):
    while Senar(num) == False:
        print("ERROR: El nombre introduït és parell")
        num = int(input("Introduir un nombre senar: "))
        
    return num

#4
    
def  MenuRPSLS():
    print("Escull entre:\n 1-Rock\n 2-Paper\n 3-Scissors\n 4-Lizard\n 5-Spock") 
    
    return None
#5
    
def LlegirNombre(minim,maxim,entrada):
    
    while (entrada > maxim or entrada < minim):
        print("ERROR: Valor fora de l'interval")
        entrada=int(input("Entra valor entre XX i YY:: "))
        
    return entrada

#6
 

def JocRPSLS(player1,player2,rock,paper,scissors,lizard,spock):

    if player1 == player2:
        guanyador = 0
    elif player1 == rock and (player2 == scissors or player2 == lizard):
        guanyador = 1
    elif player1 == paper and (player2 == rock or player2 == spock):
        guanyador = 1
    elif player1 == scissors and (player2 == paper or player2 == lizard):
        guanyador = 1
    elif player1 == lizard and (player2 == spock or player2 == paper):
        guanyador = 1
    elif player1 == spock and (player2 == scissors or player2 == rock):
        guanyador = 1
    else:
        guanyador = 2
       
    return guanyador

#7
    
def MissatgeRPSLS(player1,player2,rock,paper,scissors,lizard,spock):
    if JocRPSLS(player1,player2,rock,paper,scissors,lizard,spock) == 0:
        imp = "Empat!!!"
    elif (player1 == scissors and player2 == paper) or (player2 == scissors and player1 == paper):
        imp = "Scissors cuts Paper"
    elif (player1 == paper and player2 == rock) or (player2 == paper and player1 == rock):
        imp = "Paper covers Rock"
    elif (player1 == rock and player2 == lizard) or (player2 == rock and player1 == lizard):
        imp ="Rock crushes Lizard"
    elif (player1 == lizard and player2 == spock) or (player2 == lizard and player1 == spock):
        imp = "Lizard poisons Spock"
    elif (player1 == spock and player2 == scissors) or (player2 == spock and player1 == scissors):
        imp ="Spock smashes Scissors"
    elif (player1 == scissors and player2 == lizard) or (player2 == scissors and player1 == lizard):
        imp ="Scissors decapitates Lizard"
    elif (player1 == lizard and player2 == paper) or (player2 == lizard and player1 == paper):
        imp ="Lizard eats Paper"
    elif (player1 == paper and player2 == spock) or (player2 == paper and player1 ==spock):
        imp ="Paper disproves Spock"
    elif (player1 == spock and player2 == rock) or (player2 == spock and player1 == rock):
        imp ="Spock vaporizes Rock"
    elif (player1 == rock and player2 == scissors) or (player2 == rock and player1 == scissors):
         imp ="Rock crushes Scissors"
         
    return imp
            
#8
rock = 1 
paper = 2
scissors = 3
lizard = 4
spock = 5  
 

informacio = PresentacioJoc()
nom = input("Introdueix el teu nom: ")
random.seed(nom)
partides = int(input("Introdueix el nombre de partides: "))
part = LlegirSenar(partides)


llista1 = []
llista2 = []
sheldon = 0
nosaltres = 0
   
while sheldon < ((part//2)+1) and nosaltres < ((part//2)+1):
    ordinador = random.randint(1,5)
    menu = MenuRPSLS()
    entrada=int(input("Entra valor entre 1 i 5: "))
    jugador =  LlegirNombre(1,5,entrada)
    joc = JocRPSLS(jugador,ordinador,rock,paper,scissors,lizard,spock)
    print(MissatgeRPSLS(jugador,ordinador,rock,paper,scissors,lizard,spock))
    
    if joc == 2:
        print("Guanya Sheldon Cooper!!!")
        sheldon += 1
    elif joc == 1:
        print("Guanya "+str(nom)+"!!!")
        nosaltres += 1
   

    if ordinador == 1:
        figura1 = "Rock"
    elif ordinador == 2:
        figura1 = "Paper"
    elif ordinador == 3:
        figura1 = "Scissors"
    elif ordinador == 4:
        figura1 = "Lizard"
    elif ordinador == 5:
        figura1 = "Spock"
    llista2.append(figura1)
   
    if jugador == 1:
        figura2 = "Rock"
    elif jugador == 2:
        figura2 = "Paper"
    elif jugador == 3:
        figura2 = "Scissors"
    elif jugador == 4:
        figura2 = "Lizard"
    elif jugador == 5:
        figura2 = "Spock"
    llista1.append(figura2)
        
    print("MARCADOR -- Sheldon",sheldon,nom,nosaltres)

if sheldon < nosaltres:
    print("El guanyador és",nom)
    
else:
    print("El guanyador és Sheldon")

print(llista2)
print(llista1)









