from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField, SelectField, validators, PasswordField
from wtforms.validators import DataRequired, Length


# Form used to show an on/off menu for the Raspberry
class RaspiOff(Form):
    on_off = RadioField('Select Reboot or Shutdown', choices=[('reboot', 'Reboot'), ('shutdown', 'Shutdown')])


# Form used to configure mpd config file
class MpdConfig(Form):
    # Removed resampling and sample rate
    mp3_gapless = SelectField("Gapless mp3 Playback", choices=[('yes', 'Yes'), ('no', 'No')])
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


# Form to configure network settings
class NetworkConfig(Form):
    dhcp = SelectField("DHCP", choices=[('a', 'aaaa'), ('b', 'bbbb'), ('c', 'cccc')])
    ssid = StringField("WiFi network name", validators=[Length(min=0, max=50)])
    security = SelectField("Security", choices=[('a', 'aaaa'), ('b', 'bbbb'), ('c', 'cccc')])
    password = StringField("Password", validators=[Length(min=0, max=50)])


# Form to configure system settings
class SystemConfig(Form):
    timezone = SelectField("Timezone", choices=[('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')])
    host = StringField("Host name", validators=[Length(min=4, max=50)])
    clear_log = RadioField("Clear system logs", choices=[('yes', 'Yes'), ('no', 'No')])
    clear_play = RadioField("Clear playback history", choices=[('yes', 'Yes'), ('no', 'No')])


# Form to configure Spotify settings
class SpotifyConfig(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    bitrate = SelectField("Audio Bitrate", choices=[('high', '320 Kbps'), ('medium', '160 Kbps'), ('low', '96 Kbps')])
    volume_norm = SelectField("Volume Normalization", choices=[('yes', 'Yes'), ('no', 'No')])
    private = SelectField("Private Session", choices=[('yes', 'Yes'), ('no', 'No')])


# Form to configure Google PLay Music settings
class GoogleConfig(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    all_access = SelectField("All Access", choices=[('yes', 'Yes'), ('no', 'No')])
    bitrate = SelectField("Audio Bitrate", choices=[('high', '320 Kbps'), ('medium', '160 Kbps'), ('low', '128 Kbps')])
    device_id = StringField("Device ID", validators=[Length(min=16, max=16)])


class Dummy(Form):
    dummy = StringField("Dummy")


