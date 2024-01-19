from app.models.base_class import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Dishes(BaseModel):
    price: Mapped[str] = mapped_column(String, nullable=False)
