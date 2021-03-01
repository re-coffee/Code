from Interface import IConexao
from Credencial import Credencial as Credencial
import psycopg2 as Postgres

class Conexao:
    def __init__(self, credencial):
        self.credencial = Credencial

    def Conectar(self):
        return 

    def Desconectar(self):
        return

    def Query(self, string):
        return

    def Importar(self, listaQuery):
        return

    def Exportar(self):
        return