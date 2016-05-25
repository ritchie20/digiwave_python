from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdConfig
from raspipower import RaspiPower


@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')


@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    if form.validate_on_submit():
        form_values = form.onoff.data
        text_file = open('texto.txt', 'w')
        text_file.write(form_values)
        text_file.close()
        power = RaspiPower(form_values)
        power.reboot_shutdown()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)


@app.route('/mpdconf', methods=['GET', 'POST'])
def mpdconf():
    form = MpdConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('mpdconf.html', form=form)
