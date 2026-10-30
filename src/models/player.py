from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

# Import the Base class
from src.db.database import Base

class Player(Base):
    """
    Database model representing a player in the RPG game.
    """
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    level: Mapped[int] = mapped_column(Integer, default=1)
    gold: Mapped[int] = mapped_column(Integer, default=0)