import datetime
import json
import uuid
from typing import Any, Optional

import aiohttp
import holidays

from .config import GIGA_CHAT_AUTHORIZATION_KEY, VK_AUTHORIZATION_KEY
from .schemas import PersonalData


async def get_access_token() -> str:
    """
    Возвращает access_token

    Returns:
        str - access_token
    """

    url: str = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'

    payload: dict = {
        'scope': 'GIGACHAT_API_PERS'
    }

    headers: dict = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Basic {GIGA_CHAT_AUTHORIZATION_KEY}'
    }

    connector: aiohttp.TCPConnector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.post(url, headers=headers, data=payload) as response:
            response_data: dict = await response.json()
            return response_data['access_token']


async def generate_advice(prompt: str) -> str:
    """
    Генерирует совет дня

    Params:
        prompt: str - текстовый вопрос

    Returns:
        str - совет дня
    """

    url: str = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    access_token: str = await get_access_token()

    try:
        payload: str = json.dumps(
            {
                'model': 'GigaChat',
                'messages': [
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'stream': False,
                'repetition_penalty': 1
            }
        )

        headers: dict = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        connector: aiohttp.TCPConnector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.post(url, headers=headers, data=payload) as response:
                response_data: dict = await response.json()
                return response_data['choices'][0]['message']['content']

    except Exception as e:
        return f"Ошибка при генерации совета. {e}"


async def get_today_holiday(country_code: str) -> Optional[str]:
    """
    Получает название праздника на сегодняшний день для указанной страны.

    Params:
        country_code: Код страны.

    Returns:
         Название праздника, если он есть, иначе None.
    """

    today: datetime.date = datetime.date.today()
    country_holidays: dict = getattr(holidays, country_code)(years=[today.year])

    if today in country_holidays:
        return f'Сегодня {today}: {country_holidays.get(today)}'
    else:
        return None


async def get_personal_data(user_id: int) -> Any:
    """
    Получает информацию о пользователе VK

    Params:
        user_id: int - ID пользователя VK

    Returns:
        PersonalData - словарь с информацией о пользователе VK
    """
    url: str = (f"https://api.vk.com/method/users.get?user_ids=id{user_id}&v=5.199&fields=first_name, "
                "last_name, "
                "about, "
                "activities, "
                "bdate, "
                "books, "
                "career, "
                "city, "
                "counters, "
                "country, "
                "education, "
                "followers_count, "
                "games, "
                "has_photo, "
                "interests, "
                "music, "
                "movies, "
                "personal, "
                "relation, "
                "sex, "
                "site, "
                "status, "
                "trending, "
                "wall_default")

    connector: aiohttp.TCPConnector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers={'Authorization': f'Bearer {VK_AUTHORIZATION_KEY}'}) as response:
            response_data = await response.json()
            return PersonalData(**response_data['response'][0])
