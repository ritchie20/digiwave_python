from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdVolume, MpdBuffer, Hostname, WifiLogin, AudioOutput
from models import RaspiPower, MpdVolumeSave, MpdBufferSave, GetMpd, HostnameSave, WifiLoginSave, GetWifi


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')


# Function that routes Raspberry power handling (reboot/shutdown) and audio output
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = RaspiOff()
    form_audio = AudioOutput()
    # This "if" waits until POST is received
    if form.submit_off.data and form.validate_on_submit():
        power = RaspiPower(form.on_off.data)
        power.reboot_shutdown()
        # flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    if form_audio.submit_audio.data and form_audio.validate_on_submit():
        print form_audio.audio_output.data
        #mpd_audio_output = AudioOutputSave(form_audio.audio_output.data)
        #error_output = mpd_audio_output.audio_output_save()
        #if error_output != '':
         #   flash(error_output, 'danger')
          #  return redirect(url_for('index'))
        #else:
         #   flash('You changes has been saved!', 'success')
          #  return redirect(url_for('index'))
    return render_template('systemconfig.html', form=form, form_audio=form_audio)


# Function that routes to MPD configuration page
@app.route('/mpdconfig', methods=['GET', 'POST'])
def mpdconfig():
    form_volume = MpdVolume()
    form_buffer = MpdBuffer()
    # Validation of "volume" form
    # //////////////////////////////
    if form_volume.validate_on_submit():
        mpd_volume = MpdVolumeSave(form_volume.vol_norm.data, form_volume.replay_gain.data,
                                   str(form_volume.replaygain_preamp.data))
        error_output = mpd_volume.mpd_volume_save()
        # if error output has data, send the message to the view
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    # Validation of "buffer" form
    # ///////////////////////////
    if form_buffer.validate_on_submit():
        mpd_buffer = MpdBufferSave(form_buffer.audio_buff.data, form_buffer.buff_fill.data)
        error_output = mpd_buffer.mpd_buffer_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    return render_template('mpdconfig.html', form_volume=form_volume, form_buffer=form_buffer)


# Sending mpd dictionary to the page
@app.route('/showmpd')
def showmpd():
    result = GetMpd()
    result = result.get_mpd_params()
    return render_template('showmpd.html', result=result)


@app.route('/showwifi')
def showwifi():
    result = GetWifi()
    result = result.get_wifi_networks()
    return render_template('showwifi.html', result=result)


# Function that routes Raspberry hostname and wifi handling
@app.route('/networkconfig', methods=['GET', 'POST'])
def networkconfig():
    form_host = Hostname()
    form_wifi = WifiLogin()
    # This "if" waits until POST is received
    if form_host.submit_hostname.data and form_host.validate_on_submit():
        mpd_hostname = HostnameSave(form_host.hostname.data)
        error_output = mpd_hostname.hostname_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    if form_wifi.submit_wifi.data and form_wifi.validate_on_submit():
        mpd_wifi = WifiLoginSave(form_wifi.wifi_name.data, form_wifi.password.data)
        error_output = mpd_wifi.wifi_login_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    return render_template('networkconfig.html', form_host=form_host, form_wifi=form_wifi)
