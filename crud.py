from sqlalchemy.orm import Session

#from . import models, galleries, images
from models import *
from galleries import *
from images import *



def get_gallery(db: Session, gallery_id: int):
    return db.query(Gallery).filter(Gallery.id == gallery_id).first()


def get_gallery_by_name(db: Session, name: str):
    return db.query(Gallery).filter(Gallery.name == name).first()


def get_galleries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Gallery).offset(skip).limit(limit).all()


def create_gallery(db: Session, gallery: GalleriesBase):
    db_gallery = Gallery(description=gallery.description, name = gallery.name)
    db.add(db_gallery)
    db.commit()
    #db.refresh(db_gallery)
    return db_gallery


def get_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Image).offset(skip).limit(limit).all()


def create_gallery_image(db: Session, image: ImageCreate, gallery_id: int):
    db_image = Image(**image.dict(), gallery_id=gallery_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image