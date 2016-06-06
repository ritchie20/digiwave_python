import subprocess

class RaspiPower(object):

    def __init__(self, value):
        self.value = value

    # Method that handle Raspberry power options (reboot/shutdown)
    def reboot_shutdown(self):
        if self.value =='reboot':
            # This line calls the script "raspi_reboot.sh", which has been given root privileges on visudo file
            p = subprocess.Popen(["sudo", "/Users/oscarrubio/python/flask/digiwave/app/scripts/raspi_reboot.sh"],
                                 stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "rebooting now, bye mac", output
        elif self.value == 'shutdown':
            # This line calls the script "raspi_shutdown.sh", which has been given root privileges on visudo file
            p = subprocess.Popen(["sudo", "/Users/oscarrubio/python/flask/digiwave/app/scripts/raspi_shutdown.sh"],
                                 stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "turning off now, bye mac", output


class MpdConfigSave(object):

    def __init__(self, resampling, sample_rate, mp3_gapless, dsd_pcm, vol_norm, audio_buff, buff_fill):
        self.resampling = resampling
        self.sample_rate = sample_rate
        self.mp3_gapless = mp3_gapless
        self.dsd_pcm = dsd_pcm
        self.vol_norm = vol_norm
        self.audio_buff = audio_buff
        self.buff_fill = buff_fill

    # Changing values untouched to "default" string
    def mpd_form_scan(self):
        if self.resampling == 'disable':
            self.resampling = 'default'
        if self.sample_rate == 'a':
            self.sample_rate = 'default'
        if self.mp3_gapless == 'yes':
            self.mp3_gapless = 'default'
        if self.dsd_pcm == 'a':
            self.dsd_pcm = 'default'
        if self.vol_norm == 'yes':
            self.vol_norm = 'default'
        if self.audio_buff == '1mb':
            self.audio_buff = 'default'
        if self.buff_fill == '10':
            self.buff_fill = 'default'

    # Calling "mpd_save" script with all the form values
    def mpd_form_save(self):
        # This line calls the script "mpd_save", which has been given root privileges on visudo file
        p = subprocess.Popen(["sudo", "/scripts/mpd_save.py", self.resampling, self.sample_rate, self.mp3_gapless,
                              self.dsd_pcm, self.vol_norm, self.audio_buff, self.buff_fill], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print "rebooting now, bye mac", output





