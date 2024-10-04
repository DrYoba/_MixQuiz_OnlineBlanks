from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas import AnswerForm

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/mixquiz/7x7/{team_name}', response_class=HTMLResponse)
async def get_blanks_page(request: Request):
    return templates.TemplateResponse("blanks.html", {"request": request})

"""@router.post('/mixquiz/7x7/{team_name}', response_class=HTMLResponse)
async def post_blank_data(request: Request, form_data: AnswerForm = Depends(AnswerForm.as_form)):
    print(form_data)
    return templates.TemplateResponse("blanks.html", {"request": request})"""

@router.post('/mixquiz/7x7/{team_name}', response_class=HTMLResponse)
async def post_basic_form(request: Request, q1: str = Form(...), q2: str = Form(...)):
    print({"q1": q1, "q2": q2})
    return templates.TemplateResponse("blanks.html", {"request": request})