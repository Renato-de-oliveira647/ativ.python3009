#escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

import time
import os

print("")#pula uma linha
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%🐒♻️👽💻👽♻️🐒%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")#palhaçada
print("")#pula uma linha

n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja ver: "))  # pede ao usuário o número de termos da sequência de Fibonacci

fibonacci= [0, 1]  # Inicializa os primeiros elementos da sequência de Fibonacci

i = 1# contador para o loop

while i < n:#puxar valores da sequencia de Fibonacci
    proximo= fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)# pra dar sequência na sequencia de Fibonacci(soma dos dois ultimos numeros)
    time.sleep(0.1)  # Pausa de meio segundo para melhor visualização
    os.system("cls")
    i += 1

    print("\n")
    print("")#pula uma linha
    print("fibonacci:", fibonacci[:n])# Exibe os N primeiros elementos da sequência de Fibonacci
    print("")#pula uma linha
    print('-♻️👽💻👽♻️🛠️⚙️🧬💻🇧🇷👽♻️👽💻👽♻️♻️👽💻👽♻️🛠️⚙️🧬💻🇧🇷👽♻️👽💻👽♻️-')  # palhaçada
    print("")#pula uma linha
    print("🛠️⚙️🧬💻🇧🇷👽 Este Programa Foi Feito Por: renatooliver647@gmail.com 🛠️⚙️🧬💻🇧🇷👽")#imprime o email do criador do programa
    print("")#pula uma linha
    print("♻️👽💻👽♻️♻️👽💻👽♻️  Obrigado Por Usar Nosso Programa!♻️👽💻👽♻️♻️👽💻👽♻️")#imprime uma mensagem agradecimento a o usuario
    print("")  # pula uma linha
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%🐒♻️👽💻👽♻️🐒%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")#palhaçada
    print("----------------------💻🇧🇷👽  fim do programa  💻🇧🇷👽----------------------")  # mensagem de fim do programa
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%🐒♻️👽💻👽♻️🐒%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")#palhaçada