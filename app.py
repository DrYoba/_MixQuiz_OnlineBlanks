import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from pages.basic_router import router as basic_router
from pages.awesome_router import router as awesome_router
from pages.login_router import router as login_router
from pages.blanks_router import router as blanks_router

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(basic_router)
app.include_router(awesome_router)
app.include_router(login_router)
app.include_router(blanks_router)


if __name__ == '__main__':
    uvicorn.run(app)
