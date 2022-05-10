from pydantic import BaseModel
from images import Image


class GalleriesBase(BaseModel):
    name: str
    description: str

class GalleriesCreate(GalleriesBase):
    pass

class Galleries(GalleriesBase):
    id: int
    images: list[Image] = []

    class Config:
        orm_mode = True