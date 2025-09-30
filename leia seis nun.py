# Delesenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.Se o valor digitado for impar,desconsidere-o.

soma= 0#inicia a soma 
for i in range(6):#vai de 0 a 5
    número=int(input("Digite um número: "))#pega o número
    if número % 2 == 0:#se o número for par
        soma+= número#soma o número
print(f"A soma dos números pares é: {soma}")#mostra a soma dos números pares
#fim do programa