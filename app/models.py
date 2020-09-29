from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    status_id = db.Column(db.Integer, db.ForeignKey("statuses.id"))

    def __repr__(self):
        return f"User {self.username}"


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"Role {self.name}"
      
class Status(db.Model):
    __tablename__ = "statuses"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255))
    user_id = db.relationship("Cases", backref="role", lazy="dynamic") # admin altering the status

    def __repr__(self):
        return f"Status {self.status}"
    
class Cases(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255)) # corruption or intervention
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))
    video = db.Column(db.String(255))
    geolocation = db.Column(db.String(255))
    reporter_email = db.Column(db.Integer, db.ForeignKey("users.id"))
    status = db.Column(db.Integer, db.ForeignKey("statuses.id"))

    def __repr__(self):
        return f"Cases {self.title}"
