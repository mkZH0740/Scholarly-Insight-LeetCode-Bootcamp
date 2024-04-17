from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# initialize database instance
db = SQLAlchemy()
# initialize marshmallow instance
ma = Marshmallow()
