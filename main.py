#entrada de dados
print("Bem vindo ao conversor de medidas!")
print("1 = conversor de temperatura")
print("2 = conversor de altura")
print("3 = conversor de peso")
print("4 = conversor de distancia")

entrada = int(input ("qual conversor irá usar?"))

#redirecionamento a partir da entrada
if entrada == 1:
    exec(open("conver_temperatura.py"))