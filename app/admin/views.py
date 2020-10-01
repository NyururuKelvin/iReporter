from app.models import Case, Status
from flask import render_template, redirect, url_for
from . import admin
from .forms import StatusForm
from .. import db


@admin.route("/cases")
def listCases():

    """
    View admin root page function that returns the admin page and its data
    """

    cases = Case.query.order_by(Case.category)

    return render_template("admin/cases.html", cases=cases)


@admin.route("case/<int:id>", methods=["GET", "POST"])
def updateStatus(id):
    # case = Case.query.get(id)
    case = Case.query.get(id)

    form = StatusForm()
    if form.validate_on_submit():
        case.status_id = form.status.data

        db.session.add(case)
        db.session.commit()
        return redirect(url_for('.listCases', id=case.id))

    return render_template("admin/updateStatus.html", case=case, form=form)
