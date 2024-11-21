from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .schemas import PersonalData
from .utils import generate_advice, get_personal_data, get_today_holiday

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/advice/')
async def generate_advice_endpoint(user_id: int) -> JSONResponse:
    """Эндпоинт для генерации совета дня"""
    try:
        personal_data: PersonalData = await get_personal_data(user_id)
        holyday: str = await get_today_holiday('RU')
        prompt: str = ('Дай короткий совет на день в одно предложение. Вот данные на основе которых генерируется совет:'
                       f'\n{personal_data}, {holyday}, если указана дата рождения то дай гороскоп.\n')
        advice: str = await generate_advice(prompt)
        return JSONResponse(content={"advice": advice}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
