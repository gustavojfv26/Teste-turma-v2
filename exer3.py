# Solicita ao usuário a temperatura em Fahrenheit e converte para float
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius usando a fórmula: (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9

# Imprime o resultado da conversão
print("Temperatura em Celsius é:", celsius)