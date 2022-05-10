from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import *
from models import *
from galleries import *
from images import *
from db import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/galleries/", response_model=Galleries)
def create_galleries(gallery: GalleriesCreate, db: Session = Depends(get_db)):
    db_gallery = get_gallery_by_name(db, name=gallery.name)
    if db_gallery:
        raise HTTPException(status_code=400, detail="Gallery already exists with that name")
    return create_gallery(db=db, gallery=gallery)


@app.get("/galleries/", response_model=list[Galleries])
def read_galleries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    galleries = get_galleries(db, skip=skip, limit=limit)
    return galleries


@app.get("/galleries/{gallery_id}", response_model=Galleries)
def read_gallery(gallery_id: int, db: Session = Depends(get_db)):
    db_gallery = get_gallery(db, gallery_id=gallery_id)
    if db_gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return db_gallery


@app.post("/galleries/{gallery_id}/images/", response_model=Image)
def create_image_for_gallery(
    gallery_id: int, image: ImageCreate, db: Session = Depends(get_db)
):
    return create_gallery_image(db=db, image=image, gallery_id=gallery_id)


@app.get("/images/", response_model=list[Image])
def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    images = get_images(db, skip=skip, limit=limit)
    return images