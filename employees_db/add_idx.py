#!/usr/bin/env python

import sys
import os

def usage():
    print("usage: %s filename") % sys.argv[0]
    sys.exit(-1)

if len(sys.argv) < 2:
    usage()

fn = sys.argv[1]

if not os.path.exists(fn):
    usage()

with open(fn) as fh:
    for (i,line) in enumerate(fh):
        start = line.find('(')
        if start == 0:
            print "(", i+1, ",", line[start+1:],
        elif start > 0:
            print line[:start-1], "(", i+1, ",", line[start+1:],
        else:
            print line.strip(),
