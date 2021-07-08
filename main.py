
from helpers import gerar_palavra_secreta
if __name__ == '__main__':
    palavra_secreta = gerar_palavra_secreta()
    # For looping que imprima a palavra escondida com *******
    print("\n===Jogo da Forca===")
    print("\nA palavra é: ")
    for letra in palavra_secreta:
        print("*",end=" ")
    #Calculando o tamanho da palavra
    tamanho_da_palavra = len(palavra_secreta)
    print(f"\nA palavra tem {tamanho_da_palavra} letras")


