from pydantic import BaseModel


class ImageBase(BaseModel):
    name : str
    description : str
    location : str
    width : int
    height : int

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True