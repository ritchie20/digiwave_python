#!/usr/bin/python


# This class get the settings from mpd.conf file.
class GetMpd(object):

    def get_mpd_params(self):
        mpd_params = {}
        with open('/Users/oscar/mpd2.conf', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip('\n')
                if 'volume_normalization' in line:
                    command, value = line.split()
                    mpd_params['volume_normalization'] = value
                if 'replaygain ' in line:
                    command, value = line.split()
                    mpd_params['Replay Gain'] = value
                if 'replaygain_preamp' in line:
                    if '# ' in line:
                        comment, command, value = line.split()
                        mpd_params['Replay Gain Preamp'] = value
                    else:
                        command, value = line.split()
                        mpd_params['Replay Gain Preamp'] = value
                if 'audio_buffer_size' in line:
                    command, value = line.split()
                    mpd_params['Audio Buffer (Kb)'] = value
                if 'buffer_before_play' in line:
                    command, value = line.split()
                    mpd_params['Buffer Before Play'] = value
        return mpd_params
