#/usr/bin/python

import sys
import subprocess

text = open('textopruebafinal.txt', 'w')
text.write(sys.argv[0])
text.write(sys.argv[1])


#p = subprocess.Popen(["shutdown", "-r", "now"], stdout=subprocess.PIPE)
#        output, err = p.communicate()
#        print "hostname edited", output

