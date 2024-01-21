from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_class import BaseModel


if TYPE_CHECKING:
    from .sub_menu import SubMenu


class Dishes(BaseModel):
    price: Mapped[str] = mapped_column(String, nullable=False)
    parent_sub_menu_id: Mapped[int] = mapped_column(
        ForeignKey("submenu.id", ondelete="CASCADE")
    )
    parent_sub_menu: Mapped["SubMenu"] = relationship(
        "SubMenu", back_populates="dishes"
    )
