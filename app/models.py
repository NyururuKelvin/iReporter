from . import db

class Case(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255)) # corruption or intervention
    title = db.Column(db.String(255))
    description = db.Column(db.String(255), index = True)
    image = db.Column(db.String(255))
    video = db.Column(db.String(255))
    geolocation = db.Column(db.String(255))

    def __repr__(self):
        return f"Case {self.description}"

    @classmethod
    def get_case(cls,id):
        cases = Case.query.filter_by(id=id).all()
        return cases