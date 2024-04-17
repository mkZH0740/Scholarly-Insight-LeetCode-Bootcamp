from api.database import db, ma
from typing import List
from sqlalchemy import Integer, String, Text, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User


user_subscription_table = db.Table(
    "user_subscription_table",
    Column("user_id", ForeignKey("user_table.id"), primary_key=True),
    Column("field_id", ForeignKey("field_table.id"), primary_key=True),
)


class Field(db.Model):
    __tablename__ = "field_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # arxiv paper field name
    name: Mapped[str] = mapped_column(String(64))
    # actual name of the field
    display_name: Mapped[str] = mapped_column(Text)

    # back populated fields
    # back populated field referencing users who subscribed to this field
    subscribed_by: Mapped[List["User"]] = relationship(
        secondary=user_subscription_table,
        back_populates="subscribed_fields",
    )


class FieldSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Field
