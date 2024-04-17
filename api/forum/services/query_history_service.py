from api.database import db, ma, QueryHistory, QueryHistorySchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class QueryHistoryService(Resource):
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        query_history_schema = QueryHistorySchema()

        try:
            query_history = query_history_schema.load(data, session=db.session)
        except ValidationError as err:
            return make_err(err.messages)

        db.session.add(query_history)
        db.session.commit()

        return make_ok(query_history_schema.dump(query_history))

    def get(self, query_history_id: int):
        query_history = QueryHistory.query.get(query_history_id)

        if not query_history:
            return make_err("query history not found")

        query_history_schema = QueryHistorySchema()
        return make_ok(query_history_schema.dump(query_history))

    def delete(self, query_history_id: int):
        query_history = QueryHistory.query.get(query_history_id)

        if not query_history:
            return make_err("query history not found")

        db.session.delete(query_history)
        db.session.commit()

        return make_ok("query history deleted")
