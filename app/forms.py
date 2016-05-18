from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length

class RaspiOff(Form):
    onoff = RadioField('onoff', choices = [('reboot', 'Reboot'), ('shutdown','Shutdown')])
