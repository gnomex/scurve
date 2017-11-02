#!/usr/bin/env python

import os
import glob
import sys
import signal
import subprocess

# img_path = '../pcaps_generated_imgs2'
img_path = '../pcaps_generated_imgs'
# path = '../Pcaps'
path = '../kenner-pcaps'

PID = None

try:
    for filename in glob.glob(os.path.join(path, '*.pcap')):
        print("Reading {}".format(filename))

        try:
            # os.system("binvis -c hilbert {} {}/{}.jpg".format(filename, img_path, os.path.basename(filename)))
            proc = subprocess.Popen(["binvis -c entropy {} {}/{}_entropy.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            proc.wait()
            proc = subprocess.Popen(["binvis -c gradient {} {}/{}_gradient.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            proc.wait()
            proc = subprocess.Popen(["binvis -c hilbert {} {}/{}_hilbert.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            proc.wait()
            proc = subprocess.Popen(["binvis -c class {} {}/{}_class.jpg".format(filename, img_path, os.path.basename(filename))], shell=True)
            PID = proc.pid
            proc.wait()
        except:
            print("Something rot there, file {}".format(filename))
            if PID:
                proc.terminate()
            raise

except (KeyboardInterrupt, SystemExit):
    print("From lol: interrupt received, stopping...")
    sys.exit(-1)
