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
            return '\nThe ' + parameter + ' does not exit'
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
audio_buff = sys.argv[5]
buff_fill = sys.argv[6]


as_comment = '#'
# calling 'replace_param' with the values picked by the user
check_error = replace_param('', 'gapless_mp3_playback', mp3_gapless)
if check_error != '':
    print check_error
check_error = replace_param('', 'volume_normalization', vol_norm)
if check_error != '':
    print check_error
check_error = replace_param('', 'audio_buffer_size', audio_buff)
if check_error != '':
    print check_error
check_error = replace_param('', 'buffer_before_play', buff_fill)
if check_error != '':
    print check_error














