from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    name : str
    description : str
    location : str
    width : int
    height : int
    file: Optional[bytes]

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int
    gallery_id: int

    class Config:
        orm_mode = True