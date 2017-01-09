#!/usr/bin/python

import subprocess
import sys

"""
class GetWifi(object):

    def get_wifi_networks(self):
        # Searching for available networks
        p = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE)
        # Doing a GREP to filter by ESSID
        output = subprocess.check_output(("grep", "ESSID"), stdin=p.stdout)
        wifi_name = ""
        line_number = -1
        # Walking the output char by char
        for line in output:
            line_number += 1
            # Removing empty spaces from output
            if line != ' ':
                # Saving the output to a new String
                wifi_name += line
        # Removing "ESSID:" from the string
        wifi_name = wifi_name.replace("ESSID:","")
        # Splitting the string into a list by "\n"
        wifi_array = wifi_name.split("\n")
        return wifi_array
"""


class GetWifi(object):

    def get_wifi_networks(self):
        return "this is a dummy text"


