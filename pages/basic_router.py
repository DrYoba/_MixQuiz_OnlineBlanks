from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/basic', response_class=HTMLResponse)
async def get_basic_from(request: Request):
    return templates.TemplateResponse("basic-form.html", {"request": request})

@router.post('/basic', response_class=HTMLResponse)
async def post_basic_form(request: Request, username: str = Form(...), password: str = Form(...)):
    print(f'username: {username}')
    print(f'password: {password}')
    return templates.TemplateResponse("basic-form.html", {"request": request})