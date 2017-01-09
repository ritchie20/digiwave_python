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
            # searching for 127.0.1.1 word
            if audio_output == "usb":
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    # print line[:1]
                    if line[:1] != "#":
                        lines[line_number] = "#" + line + "\n"
            else:
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    # print line[:1]
                    if line[:1] != "#":
                        lines[line_number] = "#" + line + "\n"
                for line in lines:
                    line_number2 += 1
                    if audio_output in line:
                        parameter_found += 1
                        break
                if parameter_found == 0:
                    return 1
                    # writing hostname on the proper line
                else:
                    lines[line_number2] = 'dtoverlay=' + audio_output + '\n'
        # writing on hosts file
        with open('/Users/oscar/config.txt', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno


def save_asound(audio_output):
    # Capturing error if the file doesn't exist
    try:
        # opening hosts file as a buffer
        with open('/Users/oscar/asound.conf', 'r') as f:
            lines = f.readlines()
            line_number = -1
            parameter_found = 0
            # searching for 127.0.1.1 word
            if audio_output == "usb":
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "card" in line:
                        parameter_found += 1
                        lines[line_number] = "	card 1\n"
                if parameter_found == 0:
                    return 1
                    # writing hostname on the proper line

            else:
                for line in lines:
                    line_number += 1
                    line = line.rstrip('\n')
                    if "card" in line:
                        parameter_found += 1
                        lines[line_number] = "	card 0\n"
                if parameter_found == 0:
                    return 1
                    # writing hostname on the proper line
        # writing on hosts file
        with open('/Users/oscar/asound.conf', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno


# assigning arguments to variables
audio_output = sys.argv[1]
# print audio_output

check_error = save_config(audio_output)
if check_error == 1:
    sys.stdout.write('"Error trying to save on config.txt"')
if check_error == 2:
    sys.stdout.write('"config.txt file does not exit"')

check_error = save_asound(audio_output)
if check_error == 1:
    sys.stdout.write('"Error trying to save on asound.conf"')
if check_error == 2:
    sys.stdout.write('"asound.conf file does not exit"')
