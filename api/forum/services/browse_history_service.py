from api.database import db, ma, BrowseHistory, BrowseHistorySchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class BrowseHistoryService(Resource):
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        browse_history_schema = BrowseHistorySchema()
        try:
            browse_history = browse_history_schema.load(data, session=db.session)
        except ValidationError as err:
            return make_err(err.messages)

        db.session.add(browse_history)
        db.session.commit()

        return make_ok(browse_history_schema.dump(browse_history))

    def get(self, browse_history_id: int):
        browse_history = BrowseHistory.query.get(browse_history_id)

        if not browse_history:
            return make_err("browse history not found")

        browse_history_schema = BrowseHistorySchema()
        return make_ok(browse_history_schema.dump(browse_history))

    def delete(self, browse_history_id: int):
        browse_history = BrowseHistory.query.get(browse_history_id)

        if not browse_history:
            return make_err("browse history not found")

        db.session.delete(browse_history)
        db.session.commit()

        return make_ok("browse history deleted")
