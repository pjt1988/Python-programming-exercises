#!/usr/bin/env python

import sys
import os

with open(sys.argv[1]) as f:
	i=1
	directory = "question_"+str(i)
        if not os.path.exists(directory):
                os.makedirs(directory)
        filepath=directory+"/q_"+str(i)
	out = open(filepath,"w")
	print "Parsing frame %d" % i
	for line in f:
            if  "#----------------------------------------#" not in line: 
	        out.write(line)
            else:
                out.close()
                i+=1

		directory = "q_"+str(i-1)
		if not os.path.exists(directory):
       			os.makedirs(directory)
       		filepath=directory+"/q_"+str(i-1)
       		out = open(filepath,"w")
	print "Parsing frame %d" % i


print "done now. enjoy.."

			
