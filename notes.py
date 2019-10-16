#!/usr/bin/env python

import sys, datetime, shutil, os.path
from configparser import ConfigParser

# get file info
configfile = os.path.expandvars("$HOME/.notes.cfg")

parser = ConfigParser()
parser.read(configfile)
dirstr = os.path.expandvars(parser.get('files', 'notedir'))
fstr = parser.get('files', 'notefile')
fname = os.path.join(dirstr, fstr)

if len(sys.argv) == 1:
    try:
        f = open(fname, 'rU')
        shutil.copyfileobj(f, sys.stdout)
        f.close()
    except IOError:
        pass
else:
    f = open(fname, 'a')
    timestr = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    f.write("- %s [%s]\n" % (' '.join(sys.argv[1:]), timestr))
    f.close()