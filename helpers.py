import random
from config import TENTATIVAS_ADICIONAIS,ARQUIVO_PALAVRAS_SECRETAS
def gerar_palav_secreta ():
    """
    Função de seleção randômica de palavras no arquivo txt
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS,'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)



