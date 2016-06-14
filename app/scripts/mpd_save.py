#!/usr/bin/python

import sys

# Function that replace old value for the new one
def replace_param2(disable, parameter, value):
    # opening the file just as buffer
    with open('/Users/oscarrubio/mpd2.conf', 'r') as f:
        lines = f.readlines()
        line_number = -1
        for line in lines:
            line_number += 1
            line = line.rstrip('\n')
            if parameter in line:
                break
        lines[line_number] = disable + ' ' + parameter + '  "' + value + '"\n'
    # writing on the same file
    with open('/Users/oscarrubio/mpd2.conf', 'w') as f:
        f.writelines(lines)






resampling = sys.argv[1]
sample_rate = sys.argv[2]
mp3_gapless = sys.argv[3]
vol_norm = sys.argv[4]
audio_buff = sys.argv[5]
buff_fill = sys.argv[6]

# calling replacement function without '#' as this parameter isn't commented
comment = ''
replace_param2(comment, 'gapless_mp3_playback', mp3_gapless)














