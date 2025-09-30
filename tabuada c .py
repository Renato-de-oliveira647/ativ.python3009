#faça um programa que pergunte qual tabuada o cliente quer imprimir.
import random#biblioteca de números aleatorios  

tabuada = int(input("Digite a tabuada que você quer imprimir: "))#pega a tabuada que o usuario quer
for i in range(0, 11):#vai de um a dez
    print(f"{tabuada} x {i} = {tabuada * i}")#mostra a tabuada do número escolhido
    #fim do programa       