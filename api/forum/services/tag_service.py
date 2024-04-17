from api.database import db, ma, Tag, TagSchema
from api.utils import make_err, make_ok

from sqlalchemy import select
from marshmallow import ValidationError
from flask import request
from flask_restful import Resource


class TagService(Resource):
    def get(self, tag_id: int):
        tag = Tag.query.get(tag_id)

        if not tag:
            return make_err("tag not found")

        tag_schema = TagSchema()
        return make_ok(tag_schema.dump(tag))
