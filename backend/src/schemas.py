from typing import Optional

from pydantic import BaseModel


class PersonalData(BaseModel):
    # first_name: Optional[str] = None
    # last_name: Optional[str] = None
    # is_closed: Optional[int] = None
    about: Optional[str] = None
    # activities: Optional[str] = None
    bdate: Optional[str] = None
    books: Optional[str] = None
    # career: Optional[list] = None
    # city: Optional[dict] = None
    # counters: Optional[dict] = None
    # country: Optional[dict] = None
    # education: Optional[dict] = None
    # followers_count: int = None
    games: Optional[str] = None
    # has_photo: Optional[int] = None
    # interests: Optional[str] = None
    music: Optional[str] = None
    movies: Optional[str] = None
    # personal: Optional[dict] = None
    # relation: Optional[int] = None
    # sex: Optional[int] = None
    # status: Optional[str] = None
