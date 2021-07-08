import random
from config import TENTATIVAS_ADICIONAIS,ARQUIVO_PALAVRAS_SECRETAS
def gerar_palavra_secreta ():
    """
    Função de seleção randômica de palavras do arquivo txt
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS,'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)
def verificar_palavra_randomica (palavra_secreta,suas_tentativas,tentativa):
    """
    Verifica se a letra dada está correta
    :param palavra_secreta: Gerada co base nos arquivo palavras secretas
    :param suas_tentativas: Lista com todas as tentativas
    :param tentativas: letra inserida nessa jogada
    :return: retorna um status - acerto ou erro
    """
    status= '' #status precisa ser zerado a cada chamada da função
    acertos= 0 # Acertos precisa ser zerado a cada tentativa/jogada

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
     chences = len(palavra_secreta)
     return chances + TENTATIVAS_ADICIONAIS






