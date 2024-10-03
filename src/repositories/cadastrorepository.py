


class RepositoryRegister:
    def __init__(self):
        from src.config.connection import ConnectionDBHandler
        self.connection = ConnectionDBHandler()
        pass
    

    def insert(self, nome, email, cpf):
        from src.entities.UsersEntities import Users
        with self.connection as Connection:
           insert = Users(nome=nome, email=email, cpf=cpf)
           Connection.session.add(insert)
           Connection.session.commit()
           
           
    