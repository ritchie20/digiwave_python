#!/usr/bin/python

import sys


# Method that replace old value for the new one
def save_config(audio_output):
    # Capturing error if the file doesn't exist
    try:
        # opening hosts file as a buffer
        with open('/Users/oscar/config.txt', 'r') as f:
            lines = f.readlines()
            line_number = -1
            line_number2 = -1
            parameter_found = 0
            # if the audio is usb, all the lines needs to be a comment
            if audio_output == "usb":
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if line[:1] != "#":
                        lines[line_number] = "#" + line + "\n"
            # if the audio is hifiberry, all the lines are a comment except for the hifiberry line
            else:
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if line[:1] != "#":
                        lines[line_number] = "#" + line + "\n"
                for line in lines:
                    line_number2 += 1
                    # if audio_output is part of the file, parameter_found is enabled
                    if audio_output in line:
                        parameter_found += 1
                        break
                if parameter_found == 0:
                    return 1
                else:
                    # replacing hifiberry line with the proper output
                    lines[line_number2] = 'dtoverlay=' + audio_output + '\n'
        with open('/Users/oscar/config.txt', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno




def save_mpdconf(audio_output):
    try:
        with open('/Users/oscar/mpd2.conf', 'r') as f:
            lines = f.readlines()
            line_number = -1
            parameter_found = 0
            if audio_output == "usb":
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "hw:" in line:
                        parameter_found += 1
                        lines[line_number] = "  device  \"hw:1\"\n"
                if parameter_found == "0":
                    return 1
            else:
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "hw:" in line:
                        parameter_found += 1
                        lines[line_number] = "  device  \"hw:0\"\n"
                if parameter_found == "0":
                    return 1
        with open('/Users/oscar/mpd2.conf', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno

"""
def save_asound(audio_output):
    # Capturing error if the file doesn't exist
    try:
        # opening file as a buffer
        with open('/Users/oscar/asound.conf', 'r') as f:
            lines = f.readlines()
            line_number = -1
            parameter_found = 0
            # if audio_output is "usb", the value must be 1
            if audio_output == "usb":
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "card" in line:
                        parameter_found += 1
                        lines[line_number] = "	card 1\n"
                if parameter_found == 0:
                    return 1
            else:
                # for any hifiberry output, the value must be "0"
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "card" in line:
                        parameter_found += 1
                        lines[line_number] = "	card 0\n"
                if parameter_found == 0:
                    return 1
        with open('/Users/oscar/asound.conf', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno
"""

# assigning arguments to variables
audio_output = sys.argv[1]
# print audio_output

check_error = save_config(audio_output)
if check_error == 1:
    sys.stdout.write('"Error trying to save on config.txt"')
if check_error == 2:
    sys.stdout.write('"config.txt file does not exit"')

check_error = save_mpdconf(audio_output)
if check_error == 1:
    sys.stdout.write('"Error trying to save on asound.conf"')
if check_error == 2:
    sys.stdout.write('"asound.conf file does not exit"')
