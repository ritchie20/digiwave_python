from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdVolume, SystemConfig, MpdBuffer
from models import RaspiPower, MpdVolumeSave, SystemConfigSave, MpdBufferSave, GetMpd


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
        power = RaspiPower(form.on_off.data)
        power.reboot_shutdown()
        flash('this is a flash test, text saved')
        return redirect(url_for('index'))
    return render_template('raspioff.html', form=form)


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


# Function that routes to System configuration page
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = SystemConfig()
    if form.validate_on_submit():
        system_form = SystemConfigSave()
        system_form.system_form_save()
    return render_template('systemconfig.html', form=form)


# Sending mpd dictionary to the page
@app.route('/showmpd')
def showmpd():
    result = GetMpd()
    result = result.get_mpd_params()
    print result
    return render_template('showmpd.html', result=result)



