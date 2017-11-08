#!/usr/bin/env python

import os
import glob
import sys
import signal
import subprocess

# path = '../Pcaps'
# img_path = '../analysis/good_pcaps'
img_path = '../analysis/bad_pcaps'

PID = None

try:
    for filename in glob.glob(os.path.join(path, '*.pcap')):
        print("Reading {}".format(filename))

        try:
            # proc = subprocess.Popen(["binvis -c entropy {} {}/{}_entropy.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            # PID = proc.pid
            # proc.wait()
            # proc = subprocess.Popen(["binvis -c gradient {} {}/{}_gradient.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            # PID = proc.pid
            # proc.wait()
            proc = subprocess.Popen(["binvis -c entropy -m hcurve {} {}/{}_entropy_hcurve.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            PID = proc.pid
            proc.wait()
            # proc = subprocess.Popen(["binvis -c class {} {}/{}_class.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            # PID = proc.pid
            # proc.wait()
        except:
            print("Something rot there, file {}".format(filename))
            if PID:
                proc.terminate()
            raise

except (KeyboardInterrupt, SystemExit):
    print("From lol: interrupt received, stopping...")
    sys.exit(-1)
