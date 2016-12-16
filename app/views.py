from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdVolume, MpdBuffer, Hostname, WifiLogin
from models import RaspiPower, MpdVolumeSave, MpdBufferSave, GetMpd, HostnameSave, WifiLoginSave


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')


# Function that routes Raspberry power handling (reboot/shutdown)
@app.route('/raspioff', methods=['GET', 'POST'])
def raspioff():
    form = RaspiOff()
    form_host = Hostname()
    form_wifi = WifiLogin()
    # This "if" waits until POST is received

    if form.submit3.data and form.validate_on_submit():
        power = RaspiPower(form.on_off.data)
        power.reboot_shutdown()
        # flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    if form_host.submit1.data and form_host.validate_on_submit():
        mpd_hostname = HostnameSave(form_host.hostname.data)
        error_output = mpd_hostname.hostname_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    if form_wifi.submit2.data and form_wifi.validate_on_submit():
        mpd_wifi = WifiLoginSave(form_wifi.wifi_name.data, form_wifi.password.data)
        error_output = mpd_wifi.wifi_login_save()
        # print form_wifi.wifi_name.data
        # print form_wifi.password.data
        # print form_wifi.submit2.data
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
        # wifi = RaspiPower(form_wifi.wifi_name.data, form_wifi.password.data)
        # power.reboot_shutdown()
        # flash('this is a flash test, text saved')
        # return redirect(url_for('index'))
    return render_template('raspioff.html', form=form, form_host=form_host, form_wifi=form_wifi)


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



