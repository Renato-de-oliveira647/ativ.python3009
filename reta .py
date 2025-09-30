a= int(input("digite o primeiro valor é-->"))
b= int(input("digite segundo valor"))
c= int(input("digite o terceiro valor"))
if(a+b>c) and (a+c>b) and (b+c>a):
    print("as retas podem formar um triangulo!")
else:
    print("as retas nao podem formar um triangulo")