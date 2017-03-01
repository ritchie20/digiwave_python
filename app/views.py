from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdVolume, MpdBuffer, Hostname, WifiLogin, MpdAudioOutput, SqueezeBuffer, SqueezeDsd, \
    SqueezeOutput
from models import RaspiPower, MpdVolumeSave, MpdBufferSave, ShowMpd, HostnameSave, WifiLoginSave, ShowWifi, \
    MpdAudioSave, SqueezeBufferSave, SqueezeDsdSave, SqueezeOutputSave, ShowSqueeze


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')


# Function that deploy Raspberry system configs like power handling
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = RaspiOff()
    # if submit and validation are ok, the form is received
    if form.submit_off.data and form.validate_on_submit():
        # passing form arguments to the model object
        power = RaspiPower(form.on_off.data)
        # calling the object method
        power.reboot_shutdown()
        return redirect(url_for('index'))
    return render_template('systemconfig.html', form=form)


# Function that deploys MPD configuration page
@app.route('/mpdconfig', methods=['GET', 'POST'])
def mpdconfig():
    # all the form objects are called
    form_volume = MpdVolume()
    form_buffer = MpdBuffer()
    form_audio_output = MpdAudioOutput()
    # Validation for form_volume
    if form_volume.submit_volume.data and form_volume.validate_on_submit():
        mpd_volume = MpdVolumeSave(form_volume.vol_norm.data, form_volume.replay_gain.data,
                                   str(form_volume.replaygain_preamp.data))
        # calling the object method and checking what returns
        error_output = mpd_volume.mpd_volume_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    # Validation for form_buffer
    if form_buffer.submit_buffer.data and form_buffer.validate_on_submit():
        mpd_buffer = MpdBufferSave(form_buffer.audio_buff.data, form_buffer.buff_fill.data)
        # calling the object method and checking what returns
        error_output = mpd_buffer.mpd_buffer_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    # Validation for form_audio_output
    if form_audio_output.submit_audio.data and form_audio_output.validate_on_submit():
        mpd_audio_buffer = MpdAudioSave(form_audio_output.audio_output.data)
        # calling the object method and checking what returns
        error_output = mpd_audio_buffer.mpd_audio_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    return render_template('mpdconfig.html', form_volume=form_volume, form_buffer=form_buffer,
                           form_audio_output=form_audio_output)


# Sending mpd configuration to the view
@app.route('/showmpd')
def showmpd():
    result = ShowMpd()
    result = result.get_mpd()
    return render_template('showmpd.html', result=result)

# Sending wifi networks to the view
@app.route('/showwifi')
def showwifi():
    result = ShowWifi()
    result = result.get_wifi()
    return render_template('showwifi.html', result=result)


@app.route('/showsqueeze')
def showsqueeze():
    result = ShowSqueeze()
    result = result.get_squeeze_params()
    return render_template("showsqueeze.html", result=result)


# Function that deploys Raspberry hostname and wifi handling
@app.route('/networkconfig', methods=['GET', 'POST'])
def networkconfig():
    form_host = Hostname()
    form_wifi = WifiLogin()
    # Validation for form_host
    if form_host.submit_hostname.data and form_host.validate_on_submit():
        mpd_hostname = HostnameSave(form_host.hostname.data)
        # calling the object method and checking what returns
        error_output = mpd_hostname.hostname_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    # Validation for form_wifi
    if form_wifi.submit_wifi.data and form_wifi.validate_on_submit():
        mpd_wifi = WifiLoginSave(form_wifi.wifi_name.data, form_wifi.password.data)
        # calling the object method and checking what returns
        error_output = mpd_wifi.wifi_login_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved!', 'success')
            return redirect(url_for('index'))
    return render_template('networkconfig.html', form_host=form_host, form_wifi=form_wifi)


@app.route('/squeezeconfig', methods=['GET', 'POST'])
def squeezeconfig():
    form_squeeze_buffer = SqueezeBuffer()
    form_squeeze_output = SqueezeOutput()
    form_squeeze_dsd = SqueezeDsd()
    if form_squeeze_buffer.submit_squeeze_buffer.data and form_squeeze_buffer.validate_on_submit():
        squeeze_buffer = SqueezeBufferSave(form_squeeze_buffer.stream_buffer.data,
                                           form_squeeze_buffer.stream_buffer.data)
        error_output = squeeze_buffer.squeeze_buffer_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved', 'success')
            return redirect(url_for('index'))
    if form_squeeze_dsd.submit_squeeze_dsd.data and form_squeeze_dsd.validate_on_submit():
        squeeze_dsd = SqueezeDsdSave(form_squeeze_dsd.dsd_output.data)
        error_output = squeeze_dsd.squeeze_dsd_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved', 'success')
            return redirect(url_for('index'))
    if form_squeeze_output.submit_squeeze_audio.data and form_squeeze_output.validate_on_submit():
        squeeze_output = SqueezeOutputSave(form_squeeze_output.audio_output.data)
        error_output = squeeze_output.squeeze_output_save()
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('Your changes has been saved', 'success')
            return redirect(url_for('index'))
    return render_template('squeezeconfig.html', form_squeeze_buffer=form_squeeze_buffer,
                           form_squeeze_output=form_squeeze_output, form_squeeze_dsd=form_squeeze_dsd)
