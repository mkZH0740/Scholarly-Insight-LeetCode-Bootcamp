from api.database import db, ma, User, UserSchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class UserService(Resource):
    def post(self):
        data = request.get_json(silent=True)

        if not data:
            return make_err("invalid data")

        user_schema = UserSchema()

        try:
            user_data = user_schema.load(data, session=db.session)
        except ValidationError as err:
            return make_err(err.messages)

        db.session.add(user_data)
        db.session.commit()

        return make_ok(user_schema.dump(user_data))

    def get(self, user_id: str):
        user = User.query.filter(User.user_id == user_id).first()

        if not user:
            return make_err("user not found")

        user_schema = UserSchema()
        return make_ok(user_schema.dump(user))

    def delete(self, user_id: str):
        user = User.query.filter(User.user_id == user_id).first()

        if not user:
            return make_err("user not found")

        db.session.delete(user)
        db.session.commit()

        return make_ok("user deleted")
