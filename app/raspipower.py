import subprocess

class RaspiPower(object):

    def __init__(self, value):
        self.value = value

    def reboot_shutdown(self):
        if self.value =='reboot':
            p = subprocess.Popen(["sudo", "/Users/oscarrubio/python/flask/digiwave/app/scripts/raspipower.sh"], stdout=subprocess.PIPE )
            output, err = p.communicate()
            print "rebooting now, bye mac", output
        elif self.value == 'shutdown':
            p = subprocess.Popen(["shutdown", "-h", "now"], stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "turning off now, bye mac", output

