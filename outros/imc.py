from operator import truediv


print("programa imc")
rodar = True
while(rodar):
    try:
        print("digite o seu peso")

        peso = float(input())

        print("digite a sua altura")

        alt = float(input())

        imc = imc_function(peso, alt)

        print(imc)

        rodar = False
    except:
        print("dados incorretos")

print("finalizado")            