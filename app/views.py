from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    if form.validate_on_submit():
        valor = form.onoff.data
        archivo = open('texto.txt', 'w')
        archivo.write(valor)
        archivo.close()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)