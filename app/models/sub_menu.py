from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_class import BaseModel


if TYPE_CHECKING:
    from .menu import Menu
    from .dishes import Dishes


class SubMenu(BaseModel):

    parent_menu_id: Mapped[int] = mapped_column(
        ForeignKey("menu.id", ondelete="CASCADE")
    )
    parent_menu: Mapped["Menu"] = relationship("Menu", back_populates="sub_menu")
    available_dishes: Mapped[list["Dishes"]] = relationship(
        "Dishes", back_populates="parent_submenu"
    )
