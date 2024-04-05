from api.database import db
from datetime import datetime
from typing import List
from sqlalchemy import Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User


class QueryParam(db.Model):
    __tablename__ = "query_param_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # key of the query param
    key: Mapped[str] = mapped_column(Text)
    # value of the query param
    value: Mapped[str] = mapped_column(Text)
    # query history id of the query history this query param belongs to
    query_history_id: Mapped[int] = mapped_column(ForeignKey("query_history_table.id"))

    # back populated fields
    # back populated field referencing the query history this query param belongs to
    belongs_to: Mapped["QueryHistory"] = relationship(back_populates="query_params")


class QueryHistory(db.Model):
    __tablename__ = "query_history_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # max result option of the query
    max_result: Mapped[int] = mapped_column(Integer)
    # start option of the query
    start: Mapped[int] = mapped_column(Integer)
    # time when this query history is created
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    # user id of the user who created this query history
    query_user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    # back populated fields
    # back populated field referencing the query params this query uses
    query_params: Mapped[List["QueryParam"]] = relationship(back_populates="belongs_to")
    # back populated field referencing the user who created this query history
    queried_by: Mapped["User"] = relationship(back_populates="query_histories")
