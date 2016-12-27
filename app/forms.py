from flask_wtf import Form
from wtforms import StringField, PasswordField, RadioField, SelectField, validators, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


# Form used to show an on/off menu for the Raspberry
class RaspiOff(Form):
    on_off = RadioField('Select Reboot or Shutdown', choices=[('reboot', 'Reboot'), ('shutdown', 'Shutdown')])
    submit3 = SubmitField("Accept")


# Form to configure MPD volume and replaygain settings
class MpdVolume(Form):
    # Removed resampling and sample rate
    vol_norm = SelectField("Volume Normalization", choices=[('no', 'No'), ('yes', 'Yes')])
    replay_gain = SelectField("Replay Gain", choices=[('off', 'Off'), ('album', 'Album'), ('track', 'Track')])
    replaygain_preamp = IntegerField("Replay Gain Preamp", [validators.NumberRange(min=-15, max=15),
                                                            validators.Optional()])


# Form to configure MPD buffer settings
class MpdBuffer(Form):
    audio_buff = SelectField("Audio Buffer (KB)", choices=[('1024', '1 MB'), ('2048', '2 MB'), ('4096', '4 MB'),
                                                           ('6144', '6 MB'), ('8192', '8 MB'), ('12288', '12 MB'),
                                                           ('16384', '16 MB'), ('24456', '24 MB'), ('32768', '32 MB')])
    buff_fill = SelectField("Buffer Before Play", choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'),
                                                           ('40%', '40%'), ('50%', '50%'), ('60%', '60%'),
                                                           ('70%', '70%'), ('80%', '80%'), ('90%', '90%'),
                                                           ('100%', '100%')])


# Form to save new hostname name
class Hostname(Form):
    hostname = StringField("Hostname", [validators.length(min=4, max=30),
                                        validators.regexp('^\w+$',
                                        message="The Hostname must contain only letters, numbers or underscore")])
    submit1 = SubmitField("Accept")


class WifiLogin(Form):
    wifi_name = StringField("Wifi Name", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit2 = SubmitField("Accept")


class AudioOutput(Form):
    audio_output = SelectField("Select Audio Output", choices=[('usb', 'USB'), ('dac', 'HifiBerry DAC+'),
                                                               ('digi', 'HifiBerry Digi+'), ('amp', 'HifiBerry Amp+')])





