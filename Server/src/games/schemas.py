from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Game(Base):
    __tablename__ = "game"

    id: Mapped[int] = mapped_column(primary_key=True)
    player: Mapped[str]
    date: Mapped[str] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    result: Mapped[int]
