#escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Solicita ao usuário o número de termos da sequência de Fibonacci
import time
import os 
os.system("cls")#limpa o console para uma exbição mais limpa terminal

n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja ver: "))#pede a usuario o número de termos da sequencia de Fibonacci

# Inicializa os primeiros elementos da sequência de Fibonacci
fibonacci = [0, 1]

# Gera os próximos elementos da sequência de Fibonacci até atingir o número desejado
for i in range(2, n):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)
    time.sleep(0.5)  # Pausa de meio segundo para melhor visualização
    os.system("cls")

print( '-------------------😴🐒🐒🐒💨💨🤯🤯🤯🤯🧐----------------------')#palhaçada
print("")#pula uma linha
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%🐒🐒🐒%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")#palhaçada
print("")#pula uma linha
# Exibe os N primeiros elementos da sequência de Fibonacci
print("Os primeiros", n, "elementos da sequência de Fibonacci são:")
print("")#pula uma linha
print(fibonacci[:n])
#os.system("cls")
print( "")#pula uma linha

print("💨💨🤯🤯🤯🤯🧐 Obrigado por usar nosso programa! 💨💨🤯🤯🤯🤯🧐")#imprime uma mensagem agradecimento a o usuario
print("")#pula uma linha
print( '-------------------😴🐒🐒🐒💨💨🤯🤯🤯🤯🧐----------------------')#palhaçada