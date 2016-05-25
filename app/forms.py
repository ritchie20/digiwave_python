from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, SelectField, validators
#from wtforms.validators import DataRequired, Length


class RaspiOff(Form):
    onoff = RadioField('Select Reboot or Shutdown', choices=[('reboot', 'Reboot'), ('shutdown', 'Shutdown')])


class MpdConfig(Form):
    resampling = SelectField("Resampling", choices=[('disable', 'Disable'), ('enable', 'Enable')])
    sample_rate = SelectField("Sample rate converter",  choices=[('a', 'aaaa'), ('b', 'bbbb'), ('c', 'cccc')])
    mp3_gapless = SelectField("Gapless mp3 playback", choices=[('yes', 'Yes'), ('no', 'No')])
    dsd_pcm = SelectField("DSD over PCM", choices=[('a', 'aaaa'), ('b', 'bbbb'), ('c', 'cccc')])
    vol_norm = SelectField("Volume normalization", choices=[('yes', 'Yes'), ('no', 'No')])
    audio_buff = SelectField("Audio Buffer (KB)", choices=[('1mb', '1 MB'), ('2mb', '2 MB'), ('4mb', '4 MB'),
                                                           ('6mb', '6 MB'), ('8mb', '8 MB'), ('12mb', '12 MB'),
                                                           ('16mb', '16 MB'), ('24mb', '24 MB'), ('32mb', '32 MB')])
    buff_fill = SelectField("Buffer fill before play", choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'),
                                                                ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'),
                                                                ('90', '90'), ('100', '100')])
