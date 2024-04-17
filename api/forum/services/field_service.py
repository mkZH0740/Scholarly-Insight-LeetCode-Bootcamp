from api.database import db, ma, Field, FieldSchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class FieldService(Resource):
    def get(self, field_id: int):
        field = Field.query.get(field_id)

        if not field:
            return make_err("field not found")

        field_schema = FieldSchema()
        return make_ok(field_schema.dump(field))
