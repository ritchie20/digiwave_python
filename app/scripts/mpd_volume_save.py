#!/usr/bin/python

import sys


# Function that replace old value for the new one
def replace_param(comment, parameter, value):
    # opening the file just as buffer
    with open('/Users/oscar/mpd2.conf', 'r') as f:
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
    with open('/Users/oscar/mpd2.conf', 'w') as f:
        f.writelines(lines)


# assigning arguments to variables
vol_norm = sys.argv[1]
replay_gain = sys.argv[2]
replaygain_preamp = sys.argv[3]


as_comment = '#'
# calling 'replace_param' with the values picked by the user
check_error = replace_param('', 'volume_normalization', vol_norm)
if check_error == 'volume_normalization':
    sys.stdout.write(corruption + '"Volume normalization"')

check_error = replace_param('', 'replaygain', replay_gain)
if check_error == 'replaygain':
    sys.stdout.write(corruption + '"Replay gain"')

if replaygain_preamp == "":
    check_error = replace_param(as_comment, 'replaygain_preamp', replaygain_preamp)
    if check_error == 'replaygain_preamp':
        sys.stdout.write(corruption + '"Replay Gain Preamp"')
else:
    check_error = replace_param('', 'replaygain_preamp', replaygain_preamp)
    if check_error == 'replaygain_preamp':
        sys.stdout.write(corruption + '"Replay Gain Preamp"')

















