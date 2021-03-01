import abc

class Banco(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'Conectar') and 
                callable(subclass.Conectar) and 

                hasattr(subclass, 'Desconectar') and 
                callable(subclass.Desconectar) and

                hasattr(subclass, 'Query') and 
                callable(subclass.Query) and

                hasattr(subclass, 'Importar') and 
                callable(subclass.Importar) and

                hasattr(subclass, 'Exportar') and 
                callable(subclass.Exportar))
    
    

