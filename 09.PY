frase ="infoco consultoria e treinanamentos"
print(len(frase))#mostra o tamanho da frase conta os carater

print(frase[7])#mostra o caractrer

print(frase[7:18])#pega antes do 18

print(frase[7:18:2])#pega a primeira  1 pula pega a 2 segunda a1

print(frase[:5])#mostra de 0a 5

print(frase[21:])#mostra do21 ate o final

print(frase.count("o"))# se tive ente aspas e eletras  /conta quantidade de e os

print(frase.find("tre"))#conta carater de forma definida enter parentes

print(frase.find("etec"))#quando peço pra procura nao acha ele =-1

print("etec"in frase)#perguntamos se existe a palavra etec na frase = false

print("infoco"in frase)#perguntamos se existe a palavra infoco na frase = true


print(frase.replace("infoco","lindolfo"))#munda infoco para lindofo

print(frase.upper())#converte pra letra maiucula

print(frase.lower())#coloca em minuscula

print(frase.capitalize())#deixa aprimeira em maiusculo e as demais minuscula

print(frase.title())#coloca a primeira letra de cada palavra em maiuscula

nome ="   lindofo junior  "
nomeok=nome.strip()

print(nome)
print(nomeok)
print(len(nome))
print(len(nomeok))
print(nome.rstrip())#tira espaço da direita
print(nome.lstrip())#tira espaço da esquesda
 
#frase.split()#vai criar sua string em pedaços
#print(frase)
frase=frase.split()#vai criar sua string em pedaços
print(frase)
print(frase[2])#vai imprimir a teceira lista
print(frase[1][3])#
print("-".join(frase))#vai iprimir coloco em espaço