#!/usr/bin/python

import sys


def check_wpa():
    try:
        with open('/Users/oscar/wpa_supplicant.conf', 'r') as f:
            lines = f.readlines()
            string_found = 0
            for line in lines:
                line = line.rstrip('\n')
                if 'network=' in line:
                    string_found += 1
        return string_found
    except IOError as error:
        return -1


def save_no_params(wifi, password):
    try:
        with open('/Users/oscar/wpa_supplicant.conf', 'a') as f:
            f.write("\n\nnetwork={\n	ssid=\"" + wifi + "\"\n	psk=\"" + password + "\"\n}\n")
    except IOError as error:
        return error.errno


def save_with_params(value, parameter):
    try:
        with open('/Users/oscar/wpa_supplicant.conf', 'r') as f:
            lines = f.readlines()
            line_number = -1
            parameter_found = 0
            # searching for 127.0.1.1 word
            for line in lines:
                line_number += 1
                line = line.rstrip('\n')
                if parameter in line:
                    parameter_found += 1
                    break
        if parameter_found == 0:
            return 1
            # writing hostname on the proper line
        else:
            lines[line_number] = '	' + parameter + '=\"' + value + '\"\n'
        # writing on hosts file
        with open('/Users/oscar/wpa_supplicant.conf', 'w') as f:
            f.writelines(lines)
    except IOError as error:
        return error.errno


wifi = sys.argv[1]
password = sys.argv[2]

flag = check_wpa()
if flag == -1:
    sys.stdout.write('"wpa_supplicant.conf file does not exit"')
if flag == 0:
    check_error = save_no_params(wifi, password)
    if check_error == 2:
        sys.stdout.write('"wpa_supplicant.conf file does not exit"')
if flag > 0:
    check_error = save_with_params(wifi, "ssid")
    if check_error == 1:
        sys.stdout.write('"parameter ssid does not exist"')
    if check_error == 2:
        sys.stdout.write('"wpa_supplicant.conf file does not exist"')
    check_error = save_with_params(password, "psk")
    if check_error == 1:
        sys.stdout.write('"parameter psk does not exist"')



