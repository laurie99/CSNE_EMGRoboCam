# Main function to get BioMetric input and Missile output
# Laurie Zhang
# 10/12/14

from cameraLauncher import cameraLauncher
import sys
import time
from Mapping import Mapping

# follow along the tail of log file
def follow(thefile):
    while True:
        lines = thefile.readlines()
        if not lines:
            time.sleep(0.5)
            continue
        # set the pointer to tail
        thefile.seek(0,1)
        #yield lines
        return lines

# Split the lines into 6 channel signals
def single(text):
    input_list = text.split()
    word_list = []
    for i in range(len(input_list)):
        word_list.append(input_list[i])
    return word_list

# Put the channel signals into one list
def channel(loglines):
    # Creates a list containing 6 lists
    data = [[] for x in xrange(6)]

    for line in loglines:
        channel_list = single(line)
        #print channel_list
        for i in range(len(channel_list)):
            #print channel_list[i]
            data[i].append(channel_list[i])
    return data

def main():
    # read log file
    log_file = open(sys.argv[1],'r')
    while True:
        loglines = follow(log_file)
        data = channel(loglines)
        status = Mapping(data)
        cameraLauncher(status)

    log_file.close()

if __name__ == '__main__':
    main()
