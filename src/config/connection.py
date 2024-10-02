from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine

class ConnectionDBHandler:
    def __init_(self):
        self.engine = 'mysql+pymysql://root:lucasvieira@mysqltest/cadastro'
        self.session = None
        self.__engine = self.create_engine()
        
        
    def create_engine(self):
        engine = create_engine(self.engine)
        return engine
    
    
    def get_engine(self):
        return self.__engine()
    
    
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self
    
    
    def __exit__(self, exc_val, exc_tb, exc_type):
        return self.session.close()
    
    
    
    