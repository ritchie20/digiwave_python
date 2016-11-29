#!/usr/bin/python

import sys


# Function that replace old value for the new one
hostname = sys.argv[1]
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
        print "error!!"
    # writing hostname on the proper line
    else:
        lines[line_number] = '127.0.1.1	' + hostname + '\n'
# writing on hosts file
with open('/Users/oscar/hosts', 'w') as f:
    f.writelines(lines)

if parameter_found > 0:
    # opening the file hostname as buffer
    with open('/Users/oscar/hostname', 'r') as f:
        lines = f.readlines()
        #line_number = 0
        lines[0] = hostname
        # writing on hostname file
    with open('/Users/oscar/hostname', 'w') as f:
        f.writelines(lines)

