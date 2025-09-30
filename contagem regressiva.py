#faça um programa que mostre na tela uma contage regressivapara o estouro de fogos de artifício, indo de 10 até 0,com uma pausa de 1 segundo entre eles.

import time#bilioteca de tempo

contagem=10#iniçio da contagem

while contagem>-1:#enquanto a contagem foor maior que -1

    print (contagem)#mostra a contagem

    time.sleep(1)#pausa de 1 segundo


    contagem -= 1#diminui 1 na contagem

    print("fogo  que estouro!!!")#começou a festa

    #fim do programa 