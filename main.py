from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from repositories.produto_repo import inserir, criar_tabela
from models.produto_model import Produto
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
async def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
async def post_cadastro(
  nome: str = Form(...), 
  descricao: str = Form(...), 
  estoque: int = Form(...), 
  preco: float = Form(...), 
  categoria: str = Form(...)):
    try:
        produto = Produto(nome=nome, descricao=descricao, estoque=estoque, preco=preco, categoria=categoria)
        inserir(produto)
        return RedirectResponse(url="/cadastro_recebido", status_code=303)
    except Exception as e:
        print(f"Erro ao inserir produto: {e}")
        return RedirectResponse(url="/cadastro", status_code=303)

@app.get("/cadastro_recebido")
async def cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    criar_tabela()
    uvicorn.run("main:app", port=8000, reload=True)
