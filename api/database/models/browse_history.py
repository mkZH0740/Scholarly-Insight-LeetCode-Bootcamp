from api.database import db
from datetime import datetime
from sqlalchemy import Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User


class BrowseHistory(db.Model):
    __tablename__ = "browse_history_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # user accessed url
    url: Mapped[str] = mapped_column(Text)
    # time when user accessed the url
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    # user id of the user who created this browse history
    browse_user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    # back populated fields
    # back populated field referencing the user who created this browse history
    browsed_by: Mapped["User"] = relationship(back_populates="browse_histories")
