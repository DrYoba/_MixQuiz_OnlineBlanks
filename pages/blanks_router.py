from datetime import datetime
from random import randint
from typing import Dict
from google_sheets.google_sheet_sync_api import gm

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.background import BackgroundTasks


router = APIRouter()

templates = Jinja2Templates(directory="templates")

form_ids = {
    "round1": "form744365622",
    "round2": "form744367803",
    "round3": "form744367895",
    "round4": "form744368008",
    "round5": "form744368091",
    "round6": "form744368146",
    "round7": "form744368182",
}

@router.get('/mixquiz/7x7/{team_name}', response_class=HTMLResponse)
async def get_blanks_page(request: Request):
    return templates.TemplateResponse("blanks.html", {"request": request})

async def get_team_blank_data(
        team_name: str,
        q1: str = Form(...),
        q2: str = Form(...),
        q3: str = Form(...),
        q4: str = Form(...),
        q5: str = Form(...),
        q6: str = Form(...),
        q7: str = Form(...),
        hidden: str = Form(...),
) -> Dict[str, str]:
    formed_url = "http://127.0.0.1:8000/mixquiz/7x7/" + team_name.replace(" ", "%20")
    blank_data = {
        "answer1": q1,
        "answer2": q2,
        "answer3": q3,
        "answer4": q4,
        "answer5": q5,
        "answer6": q6,
        "answer7": q7,
        "team": team_name,
        "referer": formed_url,
        "formid": form_ids[hidden],
        "Form name": hidden,
        "sent": datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
        "requestid": f"8305763:{randint(6700000000, 6900000000)}",
    }
    return blank_data

def push_blank_data(data: Dict[str, str]):
    gm.push_data(data=data)

@router.post('/mixquiz/7x7/{team_name}', response_class=HTMLResponse)
async def post_blank_data(request: Request, background_tasks: BackgroundTasks, blank_data = Depends(get_team_blank_data)):
    background_tasks.add_task(push_blank_data, blank_data)
    return templates.TemplateResponse("blanks.html", {"request": request})