from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def paginaInicial(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
  return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(nome: str = Form(...), descricao: str = Form(...), estoque: int = Form(...), preco: float = Form(...), categoria: str = Form(...)):
  return RedirectResponse("/", status_code=303)


if __name__ == "__main__":
  uvicorn.run("main:app", port=8000, reload=True)
