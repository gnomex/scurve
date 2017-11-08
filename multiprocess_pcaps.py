#!/usr/bin/env python

import concurrent.futures
import os
import glob
import sys
import signal
import subprocess

def do_magic(filename):
    PID = None

    dst_img_file = "../analysis/good_pcaps/{}_entropy_hcurve.jpg".format(os.path.basename(filename))

    try:
        proc = subprocess.Popen(["binvis -c entropy -m hcurve {} {}".format(filename, dst_img_file)], shell=True)
        PID = proc.pid
        proc.wait()

        return dst_img_file
    except:
        print("Something rot there, file {}".format(filename))
        if PID:
            proc.terminate()
        raise

if __name__ == '__main__':
    path = '../Pcaps'

    pcap_files = glob.glob(os.path.join(path, '*.pcap'))

    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for image_file, binvis_file in zip(pcap_files, executor.map(do_magic, pcap_files)):
                print("A binvis for {} was saved as {}".format(image_file, binvis_file))

    except (KeyboardInterrupt, SystemExit):
        print("interrupt received, stopping...")
        sys.exit(-1)
