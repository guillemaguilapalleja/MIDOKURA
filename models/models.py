from typing import Optional
from sqlalchemy import BLOB, Column, ForeignKey, Integer, String, BINARY
from sqlalchemy.orm import relationship

from database import Base


class Gallery(Base):
    __tablename__ = "galleries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)

    images = relationship("Image", back_populates="galleries")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    location = Column(String, index=True)
    width = Column(Integer, index=True)
    height = Column(Integer, index=True)
    file = Column(BINARY, index = True)
    gallery_id = Column(Integer, ForeignKey("galleries.id"))

    galleries = relationship("Gallery", back_populates="images")