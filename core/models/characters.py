from ..extensions import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    full_name = db.Column(db.String(120))
    portrayed_by = db.Column(db.String(120))
    home_town = db.Column(db.String(120))
    date_of_birth = db.Column(db.Date)
    occupation = db.Column(db.String(80))
    # romances = db.relationship()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'full_name': self.full_name,
            'portrayed_by': self.portrayed_by,
            'home_town': self.home_town,
            'DoB': self.date_of_birth,
            'occupation': self.occupation
        }
