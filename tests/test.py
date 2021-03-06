from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 

from database import Base
from main import get_db, app



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test():

    #CREATE GALLERY

    response = client.post(
        "/galleries/",
        json={"name": "TestGallery", "description": "TestGallery"},
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "TestGallery"
    assert "id" in data
    gallery_id = data["id"]

    response = client.get(f"/galleries/{gallery_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "TestGallery"
    assert data["id"] == gallery_id

    #CREATE IMAGE FOR GALLERY

    response = client.post(
        f"/galleries/{gallery_id}/images/",
        json={"name": "Image1", "description": "Image1", "location": "Image1", "width": 1, "height": 1, "gallery_id": gallery_id},
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    image_id = data["id"]


    response = client.get(f"/galleries/{gallery_id}/images/{image_id}/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == image_id
    assert data["gallery_id"] == gallery_id


    #DELETE IMAGE FROM GALLERY

    response = client.delete(f"/galleries/{gallery_id}/images/{image_id}/")

    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    image_id = data["id"]

    response = client.get(f"/galleries/{gallery_id}/images/{image_id}/")
    assert response.status_code == 404, response.text

    #DELETE A GALLERY


    response = client.delete(f"/galleries/{gallery_id}/")

    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    gallery_id = data["id"]


    response = client.get(f"/galleries/{gallery_id}/")
    assert response.status_code == 404, response.text


