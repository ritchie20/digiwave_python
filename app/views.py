from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdConfig, NetworkConfig, SystemConfig, SpotifyConfig, GoogleConfig, SoundConfig
from raspipower import RaspiPower


@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')


@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    if form.validate_on_submit():
        #form_values = form.onoff.data
        text_file = open('texto.txt', 'w')
        text_file.write(form.onoff.data)
        text_file.close()
        power = RaspiPower(form.onoff.data)
        power.reboot_shutdown()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)


@app.route('/mpdconfig', methods=['GET', 'POST'])
def mpdconfig():
    form = MpdConfig()
    if form.validate_on_submit():
        text_file = open('texto2.txt', 'w')
        text_file.write(form.audio_buff.data)
        text_file.close()
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('mpdconfig.html', form=form)


@app.route('/networkconfig', methods=['GET', 'POST'])
def networkconfig():
    form = NetworkConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('networkconfig.html', form=form)


@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = SystemConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('systemconfig.html', form=form)


@app.route('/spotifyconfig', methods=['GET', 'POST'])
def spotifyconfig():
    form = SpotifyConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('spotifyconfig.html', form=form)


@app.route('/googleconfig', methods=['GET', 'POST'])
def googleconfig():
    form = GoogleConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('googleconfig.html', form=form)


@app.route('/soundconfig', methods=['GET', 'POST'])
def soundconfig():
    form = SoundConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('soundconfig.html', form=form)
