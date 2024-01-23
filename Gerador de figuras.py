# Gerador de figuras

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()

# Retorna a quantidade de referências passadas

contador = len(sys.argv)

# Com a quantidade de referências sabemos a quantidade de vezes que o código vai estar em loop

i = 1 # O contador começa no 1 pois o zero é o nome do script

while i < contador:

    mes = sys.argv[i]

    ################################################################################
    # Importa o arquivo CSV

    caminho = r'C:\Users\kenji\OneDrive\Documentos\EBAC\Ciêntista de dados\Módulo 14\SINASC_' + mes + '.csv'

    sinasc = pd.read_csv(caminho)

    ################################################################################
    # Função que gera gráficos

    def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
        if opcao == 'nada':
            pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15,5])
        elif opcao == 'unstack':
            pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15,5])
        elif opcao == 'sort':
            pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15,5])
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        return None

    ################################################################################
    # Variável que vai indicar o nome da pasta onde os gráficos serão salvos

    max_data = sinasc.DTNASC.max()[:7]

    ################################################################################
    # Cria o diretório onde serão salvas as figuras

    caminho_dir = r'C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/'
    os.makedirs(caminho_dir + max_data, exist_ok=True)

    ################################################################################
    # Roda a função e salva a figura na pasta criada

    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'quantidade de nascimento','data de nascimento')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+"/quantidade_nascimento.png")
    plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+'/media_idade_mae_sexo.png')
    plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+'/media_peso_bebe_sexo.png')
    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+'/media_apgar1_escolaridade_mae.png')
    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+'/media_apgar1_gestacao.png')
    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
    plt.savefig("C:/Users/kenji/OneDrive/Documentos/EBAC/Ciêntista de dados/Módulo 14/output/figs/"+max_data+'/media_apgar5_gestacao.png')

    i += 1