import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pessoa import Pessoa, PessoaDTO

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def ler_arquivo():
    with open('registors.json', 'r') as dados:
        try:
            return list(json.load(dados))
        except:
            return []
        
@app.get("/api/registros")
def listar_registros():
    registros = ler_arquivo()

    if not registros:
        return {"message": "Nenhum registro encontrado"}
    
    return registros

@app.post("/api/resgitros")
def adcionar_registros(dto: PessoaDTO):
    registros = ler_arquivo()

    novo_registro = {"nome": dto.nome, "nascimento": dto.nascimento}
    registros.append(novo_registro)

    with open("registros.json", "w") as dados:
        dados.write(json.dumps(registros, indent=))
