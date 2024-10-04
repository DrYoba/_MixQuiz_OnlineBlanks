from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/mixquiz/basic', response_class=HTMLResponse)
async def get_basic_from(request: Request):
    return templates.TemplateResponse("basic-form.html", {"request": request})

@router.post('/mixquiz/basic/{tn}', response_class=HTMLResponse)
async def post_basic_form(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("basic-form.html", {"request": request})