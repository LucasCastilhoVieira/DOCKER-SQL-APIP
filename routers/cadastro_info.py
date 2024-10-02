from fastapi import APIRouter


router = APIRouter(tags=['CADASTRAR'])

@router.post('/cadastro')
def cadastrar(
    nome: str,\
    email: str,\
    cpf: str):
    
    return 'CADASTRO EFEITUADO COM SUCESSO'