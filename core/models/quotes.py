from ..extensions import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, \
                          db.ForeignKey('character.id'))