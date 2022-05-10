from fastapi import Depends, FastAPI, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from crud import crud
from models import models
from schemas import Galleries, Images
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/galleries/", response_model=Galleries.Galleries)
def create_galleries(gallery: Galleries.GalleriesCreate, db: Session = Depends(get_db)):
    db_gallery = crud.get_gallery_by_name(db, name=gallery.name)
    if db_gallery:
        raise HTTPException(status_code=400, detail="Gallery already exists with that name")
    return crud.create_gallery(db=db, gallery=gallery)


@app.get("/galleries/", response_model=list[Galleries.Galleries])
def read_galleries(db: Session = Depends(get_db)):
    galleries = crud.get_galleries(db)
    return galleries


@app.get("/galleries/{gallery_id}/", response_model=Galleries.Galleries)
def read_gallery(gallery_id: int, db: Session = Depends(get_db)):
    db_gallery = crud.get_gallery_by_id(db, gallery_id=gallery_id)
    if db_gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return db_gallery

@app.delete("/galleries/{gallery_id}/", response_model=str)
def delete_a_gallery(gallery_id: int, db: Session = Depends(get_db)):
    crud.delete_gallery(db, gallery_id=gallery_id)
    return "The gallery with ID " + str(gallery_id) + " has just been deleted."
    

@app.post("/galleries/{gallery_id}/images/", response_model=str)
def create_image_for_gallery(gallery_id: int, image: Images.ImageBase, db: Session = Depends(get_db)):
    FinalImage = crud.create_gallery_image(db=db, image=image, gallery_id=gallery_id)
    return "The id of the created image is " + str(FinalImage.id) + ""


@app.get("/galleries/{gallery_id}/images/", response_model=list[Images.Image])
def read_image(gallery_id: int, db: Session = Depends(get_db)):
    images = crud.get_images_from_gallery(db=db, gallery_id=gallery_id)
    return images


@app.get("/galleries/{gallery_id}/images/{image_id}",response_model=Images.Image)
def get_image(gallery_id: int, image_id: int, db: Session = Depends(get_db)):
    image = crud.get_image_by_id(db=db,image_id=image_id, gallery_id=gallery_id)
    return image

@app.delete("/galleries/{gallery_id}/images/{image_id}", response_model=str)
def delete_an_image(gallery_id: int, image_id: int, db: Session = Depends(get_db)):
    crud.delete_image(db, image_id=image_id, gallery_id=gallery_id)
    return "The image with ID " + str(image_id) + " in the gallery with ID " + str(gallery_id) + " has just been deleted."


@app.post("/galleries/{gallery_id}/images/{image_id}/file", response_model=bytes)
def upload_a_file(file: UploadFile, gallery_id: int, image_id: int, db: Session = Depends(get_db)):
    image = crud.upload_file(file=file, gallery_id=gallery_id, image_id=image_id, db=db)
    if image.file is None:
        raise HTTPException(status_code=404, detail="Something went wrong...")
    return image.file

@app.get("/galleries/{gallery_id}/images/{image_id}/file", response_model=str)
def see_a_file(gallery_id: int, image_id: int, db: Session = Depends(get_db)):
    image = crud.see_file(gallery_id=gallery_id, image_id=image_id, db=db)
    return image.file

