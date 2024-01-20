from typing import TYPE_CHECKING

from app.models.base_class import BaseModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from .sub_menu import SubMenu


class Menu(BaseModel):
    sub_menu: Mapped[list["SubMenu"]] = relationship("SubMenu", back_populates="parent_menu")
