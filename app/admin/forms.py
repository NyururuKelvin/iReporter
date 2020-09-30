from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SubmitField, SelectField
from ..models import Status


# def status_query():
#   return Status.query


class StatusForm(FlaskForm):
    status = SelectField(
        u"Status", choices=[(1, "Received"), (2, "Processing"), (3, "Rejected"), (4, "Resolved")]
    )
    
    submit = SubmitField("Submit")
