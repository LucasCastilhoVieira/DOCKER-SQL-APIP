from fastapi import APIRouter


router = APIRouter(tags=['CADASTRAR'])

@router.post('/cadastro')
def cadastrar(
    nome: str,
    email: str,
    cpf: str):
    
        from ..repositories.cadastrorepository import RepositoryRegister
        insert = RepositoryRegister()
        insert.insert(nome, email, cpf)
        return 'CADASTRO EFEITUADO COM SUCESSO'
    
    
    