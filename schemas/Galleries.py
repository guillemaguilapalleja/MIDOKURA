from pydantic import BaseModel
from schemas import Images


class GalleriesBase(BaseModel):
    name: str
    description: str

class GalleriesCreate(GalleriesBase):
    pass

class Galleries(GalleriesBase):
    id: int
    images: list[Images.Image] = []

    class Config:
        orm_mode = True