from api.database import db
from typing import List
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .channel import Channel, channel_tag_table


class Tag(db.Model):
    __tablename__ = "tag_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # name of the tag
    name: Mapped[str] = mapped_column(Text)

    # back populated fields
    # back populated field referencing the channels this tag is tagged to
    tagged_to: Mapped[List["Channel"]] = relationship(
        secondary=channel_tag_table,
        back_populates="tags",
    )
