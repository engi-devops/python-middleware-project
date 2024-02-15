from database.db import db
from datetime import datetime

class tbl_user(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)  # Changed to BigInteger
    username = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<tbl_user %r>' % self.name