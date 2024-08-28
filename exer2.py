# Solicita ao usuário o valor de deslocamento para a criptografia
deslocamento = int(input("Digite o deslocamento: "))

# Solicita ao usuário o texto a ser criptografado
texto = input("Digite o texto a ser criptografado: ")

# Inicializa a string para armazenar o texto criptografado
texto_criptografado = ""

# Itera sobre cada caractere do texto original
for letra in texto:
    if letra.isupper():  # Verifica se o caractere é uma letra maiúscula
        # Criptografa a letra maiúscula e adiciona ao texto criptografado
        letra_criptografada = chr((ord(letra) - ord('A') + deslocamento) % 26 + ord('A'))
    elif letra.islower():  # Verifica se o caractere é uma letra minúscula
        # Criptografa a letra minúscula e adiciona ao texto criptografado
        letra_criptografada = chr((ord(letra) - ord('a') + deslocamento) % 26 + ord('a'))
    else:
        # Se o caractere não for uma letra, não altera o caractere
        letra_criptografada = letra
    
    # Adiciona o caractere criptografado ao texto criptografado
    texto_criptografado += letra_criptografada

# Imprime o texto criptografado resultante
print("Texto criptografado:", texto_criptografado)