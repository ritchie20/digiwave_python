import subprocess
from scripts.get_mpd import GetMpd


class RaspiPower(object):

    def __init__(self, value):
        self.value = value

    # Method that handle Raspberry power options (reboot/shutdown)
    def reboot_shutdown(self):
        if self.value =='reboot':
            # This line calls the script "raspi_reboot.sh", which has been given root privileges on visudo file
            p = subprocess.Popen(["sudo", "/Users/oscar/python/flask/digiwave/app/scripts/raspi_reboot.sh"],
                                 stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "rebooting now, bye mac", output
        elif self.value == 'shutdown':
            # This line calls the script "raspi_shutdown.sh", which has been given root privileges on visudo file
            p = subprocess.Popen(["sudo", "/Users/oscar/python/flask/digiwave/app/scripts/raspi_shutdown.sh"],
                                 stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "turning off now, bye mac", output


class MpdVolumeSave(object):

    def __init__(self, vol_norm, replay_gain, replaygain_preamp):
        self.vol_norm = vol_norm
        self.replay_gain = replay_gain
        self.replaygain_preamp = replaygain_preamp

    # Calling "mpd_volume_save" script with all the form values
    def mpd_volume_save(self):
        # This line calls the script "mpd_volume_save", which has been given root privileges on visudo file
        p = subprocess.Popen(["/Users/oscar/python/flask/digiwave/app/scripts/mpd_volume_save.py",
                              self.vol_norm, self.replay_gain, self.replaygain_preamp], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        return output


class MpdBufferSave(object):

    def __init__(self, audio_buff, buff_fill):
        self.audio_buff = audio_buff
        self.buff_fill = buff_fill

    # Calling "mpd_buffer_save" script with all the form values
    def mpd_buffer_save(self):
        # This line calls the script "mpd_buffer_save", which has been given root privileges on visudo file
        p = subprocess.Popen(["/Users/oscar/python/flask/digiwave/app/scripts/mpd_buffer_save.py",
                              self.audio_buff, self.buff_fill], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        return output


class ShowMpd(object):

    def get_mpd(self):
        mpd = GetMpd
        return mpd


class HostnameSave(object):

    def __init__(self, hostname):
        self.hostname = hostname

    def hostname_save(self):
        p = subprocess.Popen(["sudo", "/Users/oscar/python/flask/digiwave/app/scripts/hostname_save.py",
                              self.hostname], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        if output == "":
            p = subprocess.Popen(["sudo", "/Users/oscar/python/flask/digiwave/app/scripts/raspi_reboot.sh"],
                                 stdout=subprocess.PIPE)
            output = p.communicate()
        return output


class WifiLoginSave(object):

    def __init__(self, wifi_name, password):
        self.wifi_name = wifi_name
        self.password = password

    # Calling "mpd_volume_save" script with all the form values
    def wifi_login_save(self):
        # This line calls the script "mpd_volume_save", which has been given root privileges on visudo file
        p = subprocess.Popen(["sudo", "/Users/oscar/python/flask/digiwave/app/scripts/wifi_save.py",
                              self.wifi_name, self.password], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        return output


