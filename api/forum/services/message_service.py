from api.database import db, ma, Message, MessageSchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class MessageService(Resource):
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        message_schema = MessageSchema()

        try:
            message = message_schema.load(data, session=db.session)
        except ValidationError as err:
            return make_err(err.messages)

        db.session.add(message)
        db.session.commit()

        return make_ok(message_schema.dump(message))

    def get(self, message_id: int):
        message = Message.query.get(message_id)

        if not message:
            return make_err("message not found")

        message_schema = MessageSchema()
        return make_ok(message_schema.dump(message))

    def put(self, message_id: int):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        message = Message.query.get(message_id)

        if not message:
            return make_err("message not found")

        message_schema = MessageSchema()
        message = message_schema.load(
            data,
            session=db.session,
            instance=message,
            partial=True,
        )

        db.session.commit()

        return make_ok(message_schema.dump(message))

    def delete(self, message_id: int):
        message = Message.query.get(message_id)

        if not message:
            return make_err("message not found")

        db.session.delete(message)
        db.session.commit()

        return make_ok("message deleted")
