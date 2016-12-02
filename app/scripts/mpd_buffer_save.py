#!/usr/bin/python

import sys


# Function that replace old value for the new one
def replace_param(comment, parameter, value):
    try:
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
    except IOError as error:
        return error.errno


# assigning arguments to variables
audio_buff = sys.argv[1]
buff_fill = sys.argv[2]

as_comment = '#'
# calling 'replace_param' with the values picked by the user
check_error = replace_param('', 'audio_buffer_size', audio_buff)
if check_error == 'audio_buffer_size':
    sys.stdout.write('"Error trying to save Audio Buffer value"')
if check_error == 2:
    sys.stdout.write('"The configuration file does not exit"')

check_error = replace_param('', 'buffer_before_play', buff_fill)
if check_error == 'buffer_before_play':
    sys.stdout.write('"Error trying to save Buffer before play value"')


















