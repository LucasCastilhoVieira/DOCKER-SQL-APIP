from fastapi import FastAPI
from routers.cadastro_info import router

app = FastAPI()


app.include_router(router)

@app.get('/')
def read():
    return 'ola, mundo!'

