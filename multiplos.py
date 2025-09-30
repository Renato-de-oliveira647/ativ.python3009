#faça um programa que mostre na tela todos os números múltiplos de trés e que estejam no intervalo entre 1 e 500
for número in range(1,501):#vai de 1 a 500
    if número % 3 == 0:#se o número for múltiplo de 3
        print(número)#mostre o número
        #fim do programa