from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(64), index=True, unique=True)
    alias_hash = db.Column(db.String(128))
    flags = db.Column(db.String())
    score = db.Column(db.Integer)

    def check_hash(self, hash):
        return hash == self.alias_hash

    def __repr__(self):
        return '<Player> {}'.format(self.alias)
