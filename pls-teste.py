#!/usr/bin/env python
# coding: utf-8

# # Bibliotecas
# ---

# In[98]:


# Responsável por acessar o conteúdo das pastas
from os import listdir, path
# Responsável gerar o objeto image
from PIL import Image
# Responsável por auxiliar gerar os dados da biblioteca Pillow em matrizes
import numpy as np 
# Responsável por auxiliar na conversão do objeto image em tipo numpy.array
from matplotlib import image
# Responsável na construção do dataframe
import pandas as pd


# # Leitura de nomes das imagens
# Atente-se pelo nome da pasta que contém as imagens no diretório de usa IDE.


def __read_names(pasta):
    """
    Returns directory with filenames found in a single folder
    param folder: type string that must contain exactly the name of the folder containing files for reading
    return: list type containing file directories
    """
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
    
    return jpgs

# # Processamento de imagens (RGB)

def __read_rgb(jpgs=jpgs):
    """
    Function that returns RGB encoded data in a type tuple (r,g,b)
    return: tuple containing (r,g,b)
    """
    r,g,b = [],[],[]

    for jpg in jpgs:
        img = Image.open(jpg)
        r.append(image.imread(jpg)[0][0][0])
        g.append(image.imread(jpg)[0][0][1])
        b.append(image.imread(jpg)[0][0][2])
    return r,g,b

# # Dataframe e armazenamento de planilha com resultados

def __create_df_rgb(r = __read_rgb()[0], g = __read_rgb()[1], b = __read_rgb()[2]):
    """
    Função que gera dataframe com os valores rgb
    """
    return pd.DataFrame({'R':r,'G':g,'B':b})


# # Função show_results
# Este notebook contem a função **show_results()** que será responsável por ler uma pasta contendo imagens, 
# assim retornando um dataframe com três colunas com os valores de RGB de cada arquivo.
# Apenas chame esta função inserindo um único parâmetro, que é uma string com o nome da pasta. Como apresentado abaixo:


def show_results(pasta):
    jpgs = __read_names(pasta)
    __read_rgb()
    __create_df_rgb().to_excel('results_rgb.xlsx')
    return __create_df_rgb()

#show_results('teste')

