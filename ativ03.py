km_saida =float(input("qual o km de saida?"))
km_chegada =float(input("qual o km de chegada?"))
horas_saida =float(input("que horas ele saiu(h:7.5 para 7h30)?"))
horas_chegada =float(input("que horas ele chegou(h:16.0 para 16h00)?"))
distancia =km_chegada -km_saida
tempo_viagem = horas_chegada - horas_saida 
tempo_viagem > 0:
velocidade_media = distancia/ tempo_viagem
if    
    print(f"a velocidade media que ele andoufoi de {velocidade_media:.2f}km/h.")
else
    print("o tempo de viagem deve ser maior que 0.")