#!/usr/bin/python

import sys


# Method that replace old value for the new one
def save_hostname(user_host):
    # Capturing error if the file doesn't exist
    try:
        # opening hosts file as a buffer
        with open('/Users/oscar/hosts', 'r') as f:
            lines = f.readlines()
            line_number = -1
            parameter_found = 0
            # searching for 127.0.1.1 word
            for line in lines:
                line_number += 1
                line = line.rstrip('\n')
                if '127.0.1.1' in line:
                    parameter_found += 1
                    break
            if parameter_found == 0:
                return 1
            # writing hostname on the proper line
            else:
                lines[line_number] = '127.0.1.1	' + user_host + '\n'
        # writing on hosts file
        with open('/Users/oscar/hosts', 'w') as f:
            f.writelines(lines)
        if parameter_found > 0:
            # opening the file hostname as buffer
            with open('/Users/oscar/hostname', 'r') as f:
                lines = f.readlines()
                # Saving hostname in the fist line
                lines[0] = user_host
                # writing on hostname file
            with open('/Users/oscar/hostname', 'w') as f:
                f.writelines(lines)
    except IOError as error:
        return error.errno


# assigning arguments to variables
user_host = sys.argv[1]


# calling 'save_hostname' with the word wrote by the user
check_error = save_hostname(user_host)
if check_error == 1:
    sys.stdout.write('"Error trying to save the Hostname"')
if check_error == 2:
    sys.stdout.write('"The configuration file does not exit"')

