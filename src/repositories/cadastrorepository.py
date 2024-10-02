from ..config.connection import ConnectionDBHandler
from ..entities.UsersEntities import Users

class RepositoryRegister:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        pass
    

    def insert(self, nome, email, cpf):
        with self.connection as Connection:
           insert = Users(nome=nome, email=email, cpf=cpf)
           Connection.session.add(insert)
           Connection.session.commit()
           
           
    