from flask import render_template, url_for, flash, redirect, request
from app import app
from forms import RaspiOff, MpdVolume, SystemConfig, MpdBuffer
from models import RaspiPower, MpdVolumeSave, SystemConfigSave, MpdBufferSave


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
    form = MpdVolume()
    form_2 = MpdBuffer()
    if form.validate_on_submit():
        print form.replay_gain.data
        # Validating "replaygain_preamp" value, first if it's empty, then if the values are right
        if form.replaygain_preamp.data != "":
            if -15 > int(form.replaygain_preamp.data) or int(form.replaygain_preamp.data) > 15:
                flash("The value for Replay Gain Preamp needs to be between -15 and 15", "danger")
                return redirect(url_for('mpdconfig'))
        print form.replay_gain.data
        print "paso 1"
        mpd_form = MpdVolumeSave(form.vol_norm.data, form.replay_gain.data, form.replaygain_preamp.data)
        print "paso 2"
        error_output = mpd_form.mpd_volume_save()
        # if error output has data, send the message to the view
        if error_output != '':
            flash(error_output, 'danger')
            return redirect(url_for('index'))
        else:
            flash('You changes has been saved!', 'success')
            return redirect(url_for('index'))
    #if form_2.validate_on_submit():
     #   mpd_form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      #  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return render_template('mpdconfig.html', form=form, form_2=form_2)


# Function that routes to System configuration page
@app.route('/systemconfig', methods=['GET', 'POST'])
def systemconfig():
    form = SystemConfig()
    if form.validate_on_submit():
        system_form = SystemConfigSave()
        system_form.system_form_save()
    return render_template('systemconfig.html', form=form)


