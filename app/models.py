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
        print "saving MPD configuration", output


class NetworkConfigSave(object):

    def __init__(self, dhcp, ssid, security, password):
        self.dhcp = dhcp
        self.ssid = ssid
        self.security = security
        self.password = password

    def network_form_scan(self):
        if self.dhcp == 'a':
            self.dhcp = 'default'
        if self.security == 'a':
            self.security = 'default'


    def network_form_save(self):
        p = subprocess.Popen(["sudo", "/scripts/network_save.py", self.dhcp, self.ssid, self.security, self.password],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()
        print "saving network configuration", output


class SystemConfigSave(object):

    def __init__(self, timezone, host, clear_log, clear_play):
        self.timezone = timezone
        self.host = host
        self.clear_log = clear_log
        self.clear_play = clear_play

    def system_form_scan(self):
        if self.timezone == 'a':
            self.timezone = 'default'

    def system_form_save(self):
        p = subprocess.Popen(["sudo", "/scripts/system_save.py", self.timezone, self.host, self.clear_log,
                              self.clear_play], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print "saving system configuration", output


class SpotifyConfigSave(object):

    def __init__(self, username, password, bitrate, volume_norm, private):
        self.username = username
        self.password = password
        self.bitrate = bitrate
        self.volume_norm = volume_norm
        self.private = private

    def spotify_form_scan(self):
        if self.bitrate == 'high':
            self.bitrate = 'default'
        if self.volume_norm == 'yes':
            self.volume_norm = 'default'
        if self.private == 'yes':
            self.private = 'default'

    def spotify_form_save(self):
        p = subprocess.Popen(["sudo", "scripts/spotify_save.py", self.username, self.password, self.bitrate,
                              self.volume_norm, self.private], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print "Saving Spotify configuration", output


class GoogleConfigSave(object):

    def __init__(self, username, password, all_access, bitrate, device_id):
        self.username = username
        self.password = password
        self.all_access = all_access
        self.bitrate = bitrate
        self.device_id = device_id

    def google_form_scan(self):
        if self.all_access == 'yes':
            self.all_access = 'default'
        if self.bitrate == 'high':
            self.bitrate = 'default'

    def google_form_save(self):
        p = subprocess.Popen(["sudo", "/scripts/google_save.py", self.username, self.password, self.all_access,
                              self.bitrate, self.device_id], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print "Saving Google Play Music configuration", output





