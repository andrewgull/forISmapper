#!/usr/bin/python3
"""
read paths to reads from file and runs ismap.py on each pair of reads
"""
import sys
import subprocess

# important variables
#samples_filepaths = "/data5/bio/M.tuberculosis/Out/IS6110_new/addit_samples/samples_lin1.6_3best.filepaths"
help_message = "ISmap_batch reads paths to reads from file and runs ismap.py on each pair of reads\n" \
                "Usage: ISmap_batch.py patths_file ISsequence.fasta ref_genome.gbk"
try:
    samples_filepaths = sys.argv[1]
    if samples_filepaths == "-h":
    	print(help_message)
    	sys.exit()
except IndexError:
    samples_filepaths = input("enter samples' filepaths file > ")
#IS_sequence = "/data5/bio/M.tuberculosis/Out/IS6110_new/IS6110-4.fasta"
try:
    IS_sequence = sys.argv[2]
except IndexError:
    IS_sequence = input("IS sequence (fasta) > ")
#ref = "/data5/bio/M.tuberculosis/Out/IS6110_new/H37Rv.gbk"
try:
    ref = sys.argv[3]
except IndexError:
    ref = input("ref genome (*.gbk) > ")

ismap_exe = "/home/gulyaev/bin/IS_mapper/scripts/ismap.py"
path_arg = "/home/gulyaev/bin/IS_mapper/scripts/"

#samples_filepaths = "files.list"
#IS_sequence = "IS6110-4.fasta"
#ref = "H37Rv.gbk"
#ismap_exe = "ismap.py"

paths = [line.rstrip() for line in open(samples_filepaths)]
paths.sort()

# start ismap here for each pair of reads
stderr = open("log.txt", 'w')
n = 0
for i in range(0, len(paths), 2):
    # --bam turns on keeping the final sorted and indexed BAM files of flanking reads for comparison against the reference genome
    subprocess.call([ismap_exe, "--reads", paths[i], paths[i+1], "--queries", IS_sequence, "--typingRef", ref, "--runtype", "typing", "--output", "addit_samples", "--bam", "--path", path_arg], stderr=stderr)
    n += 1
    print("pairs %i from %i processed" %(n, len(paths)/2))

print("Finished")

