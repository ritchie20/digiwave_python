from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdConfig, NetworkConfig, SystemConfig, SpotifyConfig, GoogleConfig
from models import RaspiPower, MpdConfigSave, NetworkConfigSave, SystemConfigSave, SpotifyConfigSave, GoogleConfigSave


@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')


#def regerror(message):
 #   flash(message)
  #  return render_template("mpdconfig.html", flashType="danger")


# Function that routes Raspberry power handling (reboot/shutdown)
@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    # This "if" waits until POST is received
    if form.validate_on_submit():
        power = RaspiPower(form.on_off.data)
        power.reboot_shutdown()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)


# Function that routes to MPD configuration page
@app.route('/mpdconfig', methods=['GET', 'POST'])
def mpdconfig():
    form = MpdConfig()
    if form.validate_on_submit():
        #if int(form.audio_buff.data) > 5000000000:
         #   flash("error test")
          #  return redirect(url_for('mpdconfig'), 'warning')
        mpd_form = MpdConfigSave(form.resampling.data, form.sample_rate.data, form.mp3_gapless.data, form.vol_norm.data,
                                 form.replay_gain.data, form.audio_buff.data, form.buff_fill.data)
        error_output = mpd_form.mpd_form_save()
        # if error output has data, send the message to the view
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    return render_template('mpdconfig.html', form=form)


# Function that routes to Network configuration page
@app.route('/networkconfig', methods=['GET', 'POST'])
def networkconfig():
    form = NetworkConfig()
    if form.validate_on_submit():
        network_form = NetworkConfigSave()
        network_form.network_form_save()
    return render_template('networkconfig.html', form=form)


# Function that routes to System configuration page
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = SystemConfig()
    if form.validate_on_submit():
        system_form = SystemConfigSave()
        system_form.system_form_save()
    return render_template('systemconfig.html', form=form)


# Function that routes to Spotify login and configuration page
@app.route('/spotifyconfig', methods=['GET', 'POST'])
def spotifyconfig():
    form = SpotifyConfig()
    if form.validate_on_submit():
        spotify_form = SpotifyConfigSave()
        spotify_form.spotify_form_save()
    return render_template('spotifyconfig.html', form=form)


# Function that routes to Google Play Music login and configuration page
@app.route('/googleconfig', methods=['GET', 'POST'])
def googleconfig():
    form = GoogleConfig()
    if form.validate_on_submit():
        google_form = GoogleConfigSave()
        google_form.google_form_save()
    return render_template('googleconfig.html', form=form)

