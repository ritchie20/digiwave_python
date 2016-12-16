#!/usr/bin/python

import subprocess


class GetWifi(object):

    def get_wifi_networks(self):
        p = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE)
        output = subprocess.check_output(("grep", "ESSID"), stdin=p.stdout)
        return output

