"""
Data Scientist Jr.: Karina Gonçalves Soares
Objetivo: Aqui vamos aprender a usar a API da OpenAI.
          Através do Swagger - Uvicorn vamos
          realizar algumas queries e testar a plataforma da
          OpenAI 🤗.
"""
import os # lidar com funcionalidades do sistema
import openai # Interage com a API da OpenAI
from dotenv import load_dotenv, find_dotenv # Carrega as variáveis de ambiente do arquivo '.env'
from fastapi import FastAPI # Criação rápida de APIs
from pydantic import BaseModel # Define o modelo dos dados


app = FastAPI(title='🤗 Fazendo queries à API da OpenAI 🤗',
              version='1.0.0',
              description="""Data Scientist Jr.: Karina Gonçalves Soares""")

# Configuração da OpenAI:
# lê a chave da api da openai do arquivo .env
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

# Classe para nossa entrada:
class QueryRequest(BaseModel):
    query: str


# Rota de teste para verificar se a API está em execução:
@app.get("/")
def root():
    return {"message": "API da OpenAI está em execução 🤗!"}


# Rota para obter a resposta:
@app.post("/get_completion")
def get_completion(query: QueryRequest):
    

    messages = [{"role": "user", "content": query.query}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )

    return {"Resposta": response.choices[0].message["content"]}




# Podemo executar assim, no terminal:
# $ uvicorn main:app --host 0.0.0.0 --port 8000 --reload 

# ou assim:
 
# Executar a API usando o servidor Uvicorn:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)