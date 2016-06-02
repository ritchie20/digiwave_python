from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdConfig, NetworkConfig, SystemConfig, SpotifyConfig, GoogleConfig
from models import RaspiPower


@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')


# Function that routes Raspberry power handling (reboot/shutdown)
@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    # This "if" waits until POST is received
    if form.validate_on_submit():
        # File handling just for testing purposes
        text_file = open('texto.txt', 'w')
        text_file.write(form.onoff.data)
        text_file.close()
        power = RaspiPower(form.onoff.data)
        power.reboot_shutdown()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)


# Function that routes to MPD configuration page
@app.route('/mpdconfig', methods=['GET', 'POST'])
def mpdconfig():
    form = MpdConfig()
    if form.validate_on_submit():
        text_file = open('/etc/hosts', 'a')
        text_file.write(form.audio_buff.data)
        text_file.close()
    return render_template('mpdconfig.html', form=form)


# Function that routes to Network configuration page
@app.route('/networkconfig', methods=['GET', 'POST'])
def networkconfig():
    form = NetworkConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('networkconfig.html', form=form)


# Function that routes to System configuration page
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = SystemConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('systemconfig.html', form=form)


# Function that routes to Spotify login and configuration page
@app.route('/spotifyconfig', methods=['GET', 'POST'])
def spotifyconfig():
    form = SpotifyConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('spotifyconfig.html', form=form)


# Function that routes to Google Play Music login and configuration page
@app.route('/googleconfig', methods=['GET', 'POST'])
def googleconfig():
    form = GoogleConfig()
    #if form.validate_on_submit():
        #flash('this is a flash test, text saved')
        #return redirect(url_for('index'))
    return render_template('googleconfig.html', form=form)
