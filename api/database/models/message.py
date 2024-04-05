from api.database import db
from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .channel import Channel, channel_message_table


class Message(db.Model):
    __tablename__ = "message_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # user id of the user who created this message
    author_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    # message content
    content: Mapped[str] = mapped_column(Text)
    # time when this message is created
    created_at: Mapped[datetime] = mapped_column(DateTime)
    # time when this message is last updated
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    # whether this message is updated by the user or not
    updated: Mapped[bool] = mapped_column(Boolean)
    # message id of the message which this message replies to
    reply_to: Mapped[Optional[int]] = mapped_column(ForeignKey("message_table.id"))

    # back populate fields
    # back populated field referencing the user who created this message
    sent_by: Mapped["User"] = relationship(back_populates="sent_messages")
    # back populated field referencing the channel which this message is sent to
    sent_to: Mapped["Channel"] = relationship(
        secondary=channel_message_table,
        back_populates="messages",
    )
