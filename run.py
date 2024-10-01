from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read():
    return 'ola, mundo!'

