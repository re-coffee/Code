
from IConexao import Banco

class Conexao(Banco):
    def __init__(self, Credencial, Banco):
        self.Credencial = Credencial
        self.Banco = type(Banco)
    def Conectar(self):
        return 

    def Desconectar(self):
        return

    def Query(self):
        return

    def Importar(self):
        return

    def Exportar(self):
        return