from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas import AwesomeForm

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/mixquiz/awesome', response_class=HTMLResponse)
async def get_basic_from(request: Request):
    return templates.TemplateResponse("awesome-form.html", {"request": request})

@router.post('/mixquiz/awesome', response_class=HTMLResponse)
async def post_basic_form(request: Request, form_data: AwesomeForm = Depends(AwesomeForm.as_form)):
    print(form_data)
    return templates.TemplateResponse("awesome-form.html", {"request": request})