from . import db

class Case(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255)) # corruption or intervention
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))
    video = db.Column(db.String(255))
    geolocation = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    status_id = db.Column(db.Integer, db.ForeignKey("statuses.id"))

    def __repr__(self):
        return f"Cases {self.title}"