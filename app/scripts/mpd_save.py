#!/usr/bin/python

import sys


# Function that replace old value for the new one
def replace_param(comment, parameter, value):
    # opening the file just as buffer
    with open('/Users/oscarrubio/mpd2.conf', 'r') as f:
        lines = f.readlines()
        line_number = -1
        parameter_found = 0
        for line in lines:
            line_number += 1
            line = line.rstrip('\n')
            if parameter in line:
                parameter_found += 1
                break
        # this line means the parameter given doesn't exist, file corruption!
        if parameter_found == 0:
            return parameter
        # if 'comment' parameter it's empty, then don't save it in the file
        if comment == '':
            lines[line_number] = parameter + '  "' + value + '"\n'
        # if 'comment' isn't empty, then save it with #
        else:
            lines[line_number] = comment + ' ' + parameter + '  "' + value + '"\n'
    # writing on the same file
    with open('/Users/oscarrubio/mpd2.conf', 'w') as f:
        f.writelines(lines)


# assigning arguments to variables
resampling = sys.argv[1]
sample_rate = sys.argv[2]
mp3_gapless = sys.argv[3]
vol_norm = sys.argv[4]
replay_gain = sys.argv[5]
audio_buff = sys.argv[6]
buff_fill = sys.argv[7]


as_comment = '#'
# calling 'replace_param' with the values picked by the user
corruption = 'Impossible to save '
check_error = replace_param('', 'gapless_mp3_playback', mp3_gapless)
if check_error == 'gapless_mp3_playback':
    sys.stdout.write(corruption + '"Gapless mp3 playback"')

check_error = replace_param('', 'volume_normalization', vol_norm)
if check_error == 'volume_normalization':
    sys.stdout.write(corruption + '"Volume normalization"')

check_error = replace_param('', 'replaygain', replay_gain)
if check_error == 'replaygain':
    sys.stdout.write(corruption + '"Replay gain"')

check_error = replace_param('', 'audio_buffer_size', audio_buff)
if check_error == 'audio_buffer_size':
    sys.stdout.write(corruption + '"Audio Buffer"')

check_error = replace_param('', 'buffer_before_play', buff_fill)
if check_error == 'buffer_before_play':
    sys.stdout.write(corruption + '"Buffer before play"')

















