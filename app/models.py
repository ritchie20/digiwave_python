import subprocess

class RaspiPower(object):

    def __init__(self, value):
        self.value = value

    # Method that handle Raspberry power options (reboot/shutdown)
    def reboot_shutdown(self):
        if self.value =='reboot':
            # This line calls the script "raspipower.sh", which has been given root privileges on visudo file
            p = subprocess.Popen(["sudo", "/Users/oscarrubio/python/flask/digiwave/app/scripts/raspipower.sh"],
                                 stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "rebooting now, bye mac", output
        elif self.value == 'shutdown':
            p = subprocess.Popen(["shutdown", "-h", "now"], stdout=subprocess.PIPE)
            output, err = p.communicate()
            print "turning off now, bye mac", output

