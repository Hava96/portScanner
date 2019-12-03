import socket
from netaddr import IPNetwork
import sys
from optparse import OptionParser
rang=sys.argv[2]
parser = OptionParser()
parser.add_option("-m", "--mode", dest="mode",
                  help="f is for fastmode , s is for slow mode.")
parser.add_option("-v", "--version", dest="version",
                  help="-v version")
(options, args) = parser.parse_args()
def version():
    socket.getservbyport(int(p), "tcp")
    print ("Port: %s => service name: %s" %(int(p), socket.getservbyport(int(p))))
for i in IPNetwork(sys.argv[1]):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if options.mode == "s":
        s.settimeout(2)
    elif options.mode == "f":
        s.settimeout(0.3)
    for p in range(int(rang)):
        r = s.connect_ex((str(i), p))
        if r == 0:
            print "Scan report for ("+sys.argv[1]+")"
            print "Port {}/tcp is open".format(p)
            version()
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            pass
