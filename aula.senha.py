#iniciando  o sistema em:5,4,3,2,1 ,sistema iniciado com susseso pressione uma tecla para continuar, digite a senha 1234 , senha invalida, tente novamente, senha valida, acesso permitido, acesso negado, senha deve ter no minimo 8 caracteres, pelo menos uma letra maiuscula, uma letra minuscula, um numero e um caractere especial.
import os 
os.system("cls")
print("-----------------------------------------------------🕒​🕞​🕓​🕟​🗺️​🌎​✈️​🕟​🕔​🕠​🕕​​🕖​-------------------------------------------------------")
print("--------------------------------------------Óla seja bem vindo ao sistema de acesso----------------------------------------------------")
print("-----------------------------------------------------🙃​🤩​🤩​🤩​😍​😶‍🌫️​🥽​-------------------------------------------------------------------")
senha = input("Digite a senha: ")
while len(senha) < 4 or senha != "1234":
    print("Senha invalida, tente novamente")
    print("asseco negado")
    
    senha = input("Digite a senha: ")  
    print("asseco permitido")
# print("fim do loop")
# print("fim do programa")