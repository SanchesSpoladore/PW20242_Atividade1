from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
import sqlite3
import uvicorn
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def criar_tabela():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute(SQL_CRIAR_TABELA)
    conn.commit()
    conn.close()

@app.get("/", response_class=HTMLResponse)
def paginaInicial(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(nome: str = Form(...), descricao: str = Form(...), estoque: int = Form(...), preco: float = Form(...), categoria: str = Form(...)):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute(SQL_INSERIR, (nome, descricao, estoque, preco, categoria))
    conn.commit()
    conn.close()

    return RedirectResponse("/", status_code=303)

if __name__ == "__main__":
    criar_tabela()
    uvicorn.run("main:app", port=8000, reload=True)
