from fastapi import Form
from pydantic import BaseModel

class AwesomeForm(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(cls,
                username: str = Form(...),
                password: str = Form(...)
    ):
        return cls(
            username=username,
            password=password
        )


class AnswerForm(BaseModel):
    team_name: str
    tour_number: str
    q1: str
    q2: str
    q3: str
    q4: str
    q5: str
    q6: str
    q7: str

    @classmethod
    def as_form(cls,
                team_name: str = Form(...),
                tour_number: str = Form(...),
                q1: str = Form(...),
                q2: str = Form(...),
                q3: str = Form(...),
                q4: str = Form(...),
                q5: str = Form(...),
                q6: str = Form(...),
                q7: str = Form(...),
                ):
        return cls(
            team_name=team_name,
            tour_number=tour_number,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7
        )