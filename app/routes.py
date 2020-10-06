from app import app
from flask import render_template, redirect
from app.forms import FlagForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlagForm()

    if form.validate_on_submit():
        return redirect('/doneit');

    return render_template('index.html', form=form)
