from api.database import db
from typing import List
from datetime import datetime
from sqlalchemy import Integer, Text, DateTime, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .message import Message
from .tag import Tag


channel_message_table = db.Table(
    "channel_message_table",
    Column("channel_id", ForeignKey("channel_table.id"), primary_key=True),
    Column("message_id", ForeignKey("message_table.id"), primary_key=True),
)

channel_tag_table = db.Table(
    "channel_tag_table",
    Column("channel_id", ForeignKey("channel_table.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag_table.id"), primary_key=True),
)


class Channel(db.Model):
    __tablename__ = "channel_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # name of the channel
    name: Mapped[str] = mapped_column(Text)
    # time when this channel is created
    created_at: Mapped[datetime] = mapped_column(DateTime)
    # user id of the user who created this channel
    creator_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    # user id of the user who currently own this channel
    owner_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    # back populated fields
    # back populated field referencing the user who created this channel
    created_by: Mapped["User"] = relationship(back_populates="created_channels")
    # back populated field referencing the user who currently own this channel
    owned_by: Mapped["User"] = relationship(back_populates="owned_channels")
    # back populated field referencing the messages sent to this channel
    messages: Mapped[List["Message"]] = relationship(
        secondary=channel_message_table,
        back_populates="sent_to",
        cascade="all, delete",
        passive_deletes=True,
    )
    # back populated field referencing the tags tagged to this channel
    tags: Mapped[List["Tag"]] = relationship(
        secondary=channel_tag_table,
        back_populates="tagged_to",
    )
