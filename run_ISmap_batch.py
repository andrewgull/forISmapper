#!/usr/bin/env python3
"""
read paths to reads from file and runs ismap.py on each pair of reads
"""
import sys
import subprocess
import datetime
import getpass

help_message = "ISmap_batch reads paths to fastq reads from file and runs ismap.py (v0.1.5.1) on each pair of reads\n" \
                "Arguments:\n1. - samples' filepaths file (one path per line)\n2. - IS-sequence (fasta)\n3. - reference genome (gbk)\n4. - threads for BWA"

if len(sys.argv) < 3:
    print(help_message)
    sys.exit()


samples_filepaths = sys.argv[1]
IS_sequence = sys.argv[2]
ref = sys.argv[3]
threads = sys.argv[4]

user_name = getpass.getuser()

ismap_exe = "/home/%s/bin/IS_mapper-0.1.5.1/scripts/ismap.py" % user_name
path_arg = "/home/%s/bin/IS_mapper-0.1.5.1/scripts/" % user_name

paths = [line.rstrip() for line in open(samples_filepaths)]
paths.sort()

now = datetime.datetime.now()
time_now = (str(now.year), str(now.month), str(now.day), str(now.hour), str(now.minute))

# start ismap here for each pair of reads
stderr = open("log_ismap_batch_%s.txt" % "-".join(time_now), 'w')

n = 0
for i in range(0, len(paths), 2):
    subprocess.call([ismap_exe, "--reads", paths[i], paths[i+1], "--queries", IS_sequence, "--typingRef", ref, "--runtype", "typing", "--output", "addit_samples", "--bam", "--path", path_arg], stderr=stderr)
    n += 1
    print("pairs %i from %i processed" %(n, len(paths)/2))

print("Finished")
