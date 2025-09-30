ano = int(input("digite umm ano para verificarse e bissexto:"))
if(ano% 4 == 0 and ano % 100!= 0)or (ano% 400 ==0):
    print (f"o ano -->{ano} e bissexto.")
else:
    print(f"o ano--> {ano} nao e bissexto.")
    