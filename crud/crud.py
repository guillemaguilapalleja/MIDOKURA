from fastapi import File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from models import models
from schemas import Galleries, Images



def get_gallery_by_id(db: Session, gallery_id: int):
    return db.query(models.Gallery).filter(models.Gallery.id == gallery_id).first()


def get_gallery_by_name(db: Session, name: str):
    return db.query(models.Gallery).filter(models.Gallery.name == name).first()


def get_galleries(db: Session):
    return db.query(models.Gallery).all()


def create_gallery(db: Session, gallery: Galleries.GalleriesBase):
    db_gallery = models.Gallery(description=gallery.description, name = gallery.name)
    db.add(db_gallery)
    db.commit()
    db.refresh(db_gallery)
    return db_gallery


def get_images(db: Session):
    return db.query(models.Image).all()


def create_gallery_image(db: Session, image: Images.ImageCreate, gallery_id: int):
    db_image = models.Image(name=image.name, description=image.description,
    location=image.location, width=image.width, height=image.height, gallery_id=gallery_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def delete_gallery(db: Session, gallery_id: int):
    db_to_delete = db.query(models.Gallery).filter(models.Gallery.id == gallery_id).first()
    if db_to_delete is None:
        raise HTTPException(status_code=404, detail="Cannot delete this gallery because it doesnt exist")
    db.delete(db_to_delete)
    db.commit()
    return db_to_delete

def get_images_from_gallery(db: Session, gallery_id: int):
    gallery = db.query(models.Gallery).filter(models.Gallery.id == gallery_id).first()
    if gallery is None:
        raise HTTPException(status_code=404, detail="Theres no gallery with that id")
    return gallery.images

def get_image_by_id(db: Session, image_id: int, gallery_id: int):
    gallery = db.query(models.Gallery).filter(models.Gallery.id == gallery_id).first()
    if gallery is None:
        raise HTTPException(status_code=404, detail="Theres no gallery with that id")
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if image is None:
        raise HTTPException(status_code=404, detail="Theres no image with that id in that gallery")
    return image

def delete_image(db: Session, gallery_id:str, image_id: int):
    image_from_gallery = get_image_by_id(db=db, image_id=image_id, gallery_id=gallery_id)
    db.delete(image_from_gallery)
    db.commit()
    return image_from_gallery

def upload_file(file: UploadFile, gallery_id: int, image_id: int, db: Session):
    image = get_image_by_id(gallery_id=gallery_id, image_id=image_id, db=db)
    if image.file is None:
        image.file = file
        db.refresh(image)
        db.commit()
        return image
    raise HTTPException(status_code=400, detail="Can't upload the file attached to the image.")


def see_file(gallery_id: int, image_id: int, db: Session):
    image = get_image_by_id(gallery_id=gallery_id, image_id=image_id, db=db)
    return image.file




