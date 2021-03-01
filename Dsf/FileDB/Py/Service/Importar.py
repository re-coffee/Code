import Classe.Conexao as Con, Classe.Credencial as Cre, Criptografia as Cri

def Importar(self, Con, Cre, lista):
    Con = Con(Cre).Conectar
    print(Con.Importar())
    Con.Desconectar()