from src.games.schemas import Base

from sqlalchemy.orm import Mapped, mapped_column

class Player(Base):
    __tablename__ = "player"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str, 30] = mapped_column(unique=True)