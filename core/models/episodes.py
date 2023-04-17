from ..extensions import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_number = db.Column(db.Integer)
    episode_number = db.Column(db.Integer)
    first_aired = db.Column(db.Date)
    director = db.Column(db.String(80))
    episode_name = db.Column(db.String(80))

    def format_episode_code(self):
        ep_num_string = str(self.episode_number)
        seas_num_string = str(self.season_number)
        if self.episode_number < 10:
            ep_num_string = f'0{ep_num_string}'

        return f'S{seas_num_string}xEP{ep_num_string}'

    def to_dict(self):
        return {
            'id': self.id,
            'episode': self.format_episode_code(),
            'first_aired': self.first_aired,
            'director': self.director.title(),
            'episode_name': self.episode_name.title()
        }