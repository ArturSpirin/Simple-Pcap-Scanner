__author__ = 'Artur Spirin'

import os, sys

class Scan:


    def __init__(self, pcapFile=None):

        self.file = pcapFile
        self.keyWords = []

        argNum = len(sys.argv)
        print "Got", argNum, "arguments"

        if(argNum > 1):
            if(".pcap" in sys.argv[1]):
                self.file = sys.argv[1]
                count = 1
                if(argNum > 2):
                    while count != argNum-1:
                        count+=1
                        self.keyWords.append(sys.argv[count])
                else:
                    self.keyWords = [".us","anchorfree","hotspotshield","hss","rss2search", "hsselite", "vpn"]
            else: print "using default"

        print "Working with file:", self.file
        print "Using key words: ", self.keyWords

    def pcap(self):

        tsharkHome = os.getenv("TSHARK_HOME")
        if(tsharkHome==None): print "TSHARK_HOME not found! Make sure to set TSHARK_HOME env variable."
        else: print "TSHARK_HOME found at:", tsharkHome

        if "tshark" not in tsharkHome: tsharkHome += "/tshark"
        os.system('{} -V -r {} > pcapText.txt'.format(tsharkHome, self.file))

        with open('pcapText.txt', 'r+') as File:
            data = File.read().splitlines()
            for line in data:
                for key in self.keyWords:
                    if key in line.lower():
                        print "Found: ", key, " in line: ",line

Scan().pcap()
