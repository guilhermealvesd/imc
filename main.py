#Entrada de Dados

nome = input('Informe o seu nome: ')
peso = str(input('Informe o seu peso: ')).replace(',','.')
altura = str(input('Informe a sua altura: ')).replace(',','.')

#Conversão do peso

peso = float(peso)

#Conversão da altura

altura = float(altura)

#Calculando o IMC

imc = peso / (altura ** 2)

#Categorias do peso

if imc < 17:
    print(f'{nome} está muito abaixo do peso normal.')
elif imc < 18.5:
    print(f'{nome} está abaixo do peso normal.')
elif imc < 25:
    print(f'{nome} está com peso normal.')
elif imc < 30:
    print(f'{nome} está com excesso do peso.')
elif imc < 35:
    print(f'{nome} está com obesidade classe I.')
elif imc < 40:
    print(f'{nome} está com obesidade classe II.')
else:
    print(f'{nome} está com obesidade classe III.')