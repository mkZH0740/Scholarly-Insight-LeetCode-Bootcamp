from api.database import db, ma, Channel, ChannelSchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class ChannelService(Resource):
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        channel_schema = ChannelSchema()

        try:
            channel = channel_schema.load(data, session=db.session)
        except ValidationError as err:
            return make_err(err.messages)

        db.session.add(channel)
        db.session.commit()

        return make_ok(channel_schema.dump(channel))

    def get(self, channel_id: int):
        channel = Channel.query.get(channel_id)

        if not channel:
            return make_err("channel not found")

        channel_schema = ChannelSchema()
        return make_ok(channel_schema.dump(channel))

    def put(self, channel_id: int):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        channel = Channel.query.get(channel_id)

        if not channel:
            return make_err("channel not found")

        channel_schema = ChannelSchema()
        channel = channel_schema.load(
            data, session=db.session, instance=channel, partial=True
        )

        db.session.commit()

        return make_ok(channel_schema.dump(channel))

    def delete(self, channel_id: int):
        channel = Channel.query.get(channel_id)

        if not channel:
            return make_err("channel not found")

        db.session.delete(channel)
        db.session.commit()

        return make_ok("channel deleted")
