#!/usr/bin/python

import subprocess
import sys


class GetWifi(object):

    #def get_wifi_networks(self):
     #   p = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE)
      #  output = subprocess.check_output(("grep", "ESSID"), stdin=p.stdout)
       # return output


    # !/usr/bin/python

    import sys

    def get_wifi_networks(self):
        wifi_array = []
        with open('/Users/oscar/wifi_dummy.out', 'r') as f:
            lines = f.readlines()
            line_number = -1
            for line in lines:
                line_number += 1
                line = line.rstrip('\n')
                line = line.lstrip()
                wifi_array.insert(line_number, line[6:])

        return wifi_array


