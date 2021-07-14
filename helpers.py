import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS


def gerar_palavra_secreta():
    """
    Função de seleção randômica de palavras do arquivo txt
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)


def verificar_palavra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    Verifica se a letra dada está correta
    :param palavra_secreta: Gerada co base nos arquivo palavras secretas
    :param suas_tentativas: Lista com todas as tentativas
    :param tentativas: letra inserida nessa jogada
    :return: retorna um status - acerto ou erro
    """
    status = ''  # status precisa ser zerado a cada chamada da função
    acertos = 0  # Acertos precisa ser zerado a cada tentativa/jogada

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
        else:
            status += '*'

        if letra.lower() == tentativa.lower():
            acertos += 1

    print(f"\nAcertou {acertos} letra(s), {'tentativa'}")
    return status


def total_tentativas(palavra_secreta):
    """
    Define o total de tentativas de acordo a palavra secreta
    :param palavra_secreta: gerala aleatoriamente
    :return: quantidade de tentativas
    """
    chances = len(palavra_secreta)
    return chances + TENTATIVAS_ADICIONAIS


def jogo(palavra_secreta):
    """
    Função principal do jogo
    :param palavra_secreta:palavra secreta gerada apartir do arquivo texto
    """
    chute = 0
    advinhados = False
    suas_tentativas = []
    chances = total_tentativas(palavra_secreta)
    total_chances = chances

    print(f"Total de chances: {chances}")
    while chute < total_chances:
        letra_tentativa = input(f"\nEntre sua letra: ")

        # Diminuindo as chances de 1 a 1
        chances -= 1

        # Se a letra ja foi informada/advinhada
        if letra_tentativa in suas_tentativas:
            print(f"***Atenção você ja digitou essa letra***")
            # certificando que é só uma letra e não 2
        elif len(letra_tentativa) == 1:
            # Adicionando a letra no local correto da palavra
            suas_tentativas.append(letra_tentativa)

            resultado = verificar_palavra_informada(palavra_secreta, suas_tentativas, letra_tentativa)
            if resultado == palavra_secreta:
                advinhados = True
                print(f"\n===Parabéns você venceu ! A palavra é {palavra_secreta}===")
                break

            else:
                print(f"\n- {' '.join(resultado)}")

        else:
            print(f"Entrada incorreta, informe somente uma letra.")
        # Mostrar tentativas restantes
        print(f"- Tentativas restantes {chances}")
        chute += 1
    if chute == total_chances:
        print(f"\n*** Suas tentativas acabaram, a palavra secreta é {palavra_secreta} ***")
