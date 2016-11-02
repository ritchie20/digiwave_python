from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField, SelectField, validators, PasswordField
from wtforms.validators import DataRequired, Length


# Form used to show an on/off menu for the Raspberry
class RaspiOff(Form):
    on_off = RadioField('Select Reboot or Shutdown', choices=[('reboot', 'Reboot'), ('shutdown', 'Shutdown')])


# Form to configure MPD volume and replaygain settings
class MpdVolume(Form):
    # Removed resampling and sample rate
    vol_norm = SelectField("Volume Normalization", choices=[('no', 'No'), ('yes', 'Yes')])
    replay_gain = SelectField("Replay Gain", choices=[('off', 'Off'), ('album', 'Album'), ('track', 'Track')])
    replaygain_preamp = StringField("Replay Gain Preamp", validators=[Length(min=0, max=3)])
    audio_buff = SelectField("Audio Buffer (KB)", choices=[('1024', '1 MB'), ('2048', '2 MB'), ('4096', '4 MB'),
                                                           ('6144', '6 MB'), ('8192', '8 MB'), ('12288', '12 MB'),
                                                           ('16384', '16 MB'), ('24456', '24 MB'), ('32768', '32 MB')])
    buff_fill = SelectField("Buffer Before Play", choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'),
                                                           ('40%', '40%'), ('50%', '50%'), ('60%', '60%'),
                                                           ('70%', '70%'), ('80%', '80%'), ('90%', '90%'),
                                                           ('100%', '100%')])


# Form to configure system settings
class SystemConfig(Form):
    timezone = SelectField("Timezone", choices=[('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')])
    host = StringField("Host name", validators=[Length(min=4, max=50)])
    clear_log = RadioField("Clear system logs", choices=[('yes', 'Yes'), ('no', 'No')])
    clear_play = RadioField("Clear playback history", choices=[('yes', 'Yes'), ('no', 'No')])


# Form to configure MPD buffer settings
class MpdBuffer(Form):
    audio_buff = SelectField("Audio Buffer (KB)", choices=[('1024', '1 MB'), ('2048', '2 MB'), ('4096', '4 MB'),
                                                           ('6144', '6 MB'), ('8192', '8 MB'), ('12288', '12 MB'),
                                                           ('16384', '16 MB'), ('24456', '24 MB'), ('32768', '32 MB')])
    buff_fill = SelectField("Buffer Before Play", choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'),
                                                           ('40%', '40%'), ('50%', '50%'), ('60%', '60%'),
                                                           ('70%', '70%'), ('80%', '80%'), ('90%', '90%'),
                                                           ('100%', '100%')])

