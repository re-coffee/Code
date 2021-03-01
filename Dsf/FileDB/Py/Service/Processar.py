import os
def Processar():
    caminho = os.getcwd() + "/Service/Processamento/"
    conexao = open(caminho + "Conexao.txt","r")
    arquivo = open(caminho + "Arquivo.txt","r")

    