from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


metadata = MetaData()


@as_declarative()
class Base:
    id: int
    __name__: str
    metadata = MetaData()

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
