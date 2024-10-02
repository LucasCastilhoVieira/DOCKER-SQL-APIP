from fastapi import APIRouter
from ..src.repositories.cadastrorepository import RepositoryRegister

router = APIRouter(tags=['CADASTRAR'])

@router.post('/cadastro')
def cadastrar(
    nome: str,
    email: str,
    cpf: str):
    
    
    try: 
        insert = RepositoryRegister()
        insert.insert(nome, email, cpf)
        return 'CADASTRO EFEITUADO COM SUCESSO'
    
    
    except:
        return 'erro'
    