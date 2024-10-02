from ..config.base import Base
from sqlalchemy import Column, VARCHAR

class Users(Base):
    __tablename__ = 'cadastrousuarios'
    nome = Column(VARCHAR(40))
    email = Column(VARCHAR(40))
    cpf = Column(VARCHAR(12), primary_key=True)
    
    
    
    
    