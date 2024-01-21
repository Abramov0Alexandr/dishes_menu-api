from uuid import UUID

from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

metadata = MetaData()


@as_declarative()
class Base:
    id: UUID
    __name__: str
    metadata = MetaData()

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
