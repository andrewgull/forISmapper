#!/usr/bin/python3
"""
to add '*_removedHits.txt' data to '*_table.txt'

@author: andrew
"""
import os
import csv
#pattern = input("what pattern for files to use? > ")
pattern = "_table.txt"
removedHits = [item for item in os.listdir() if "removedHits" in item]
tables = [item for item in os.listdir() if (pattern in item and "lock" not in item)]

removedHits.sort()
tables.sort()

tablehits = dict(zip(tables, removedHits))
row_to_add = ["", "", "[-]", "0", "0","[-]", "0", "0", "no"]

            
def check_gap(x):
    if x < 0:
        g = "R"
    else:
        g = "F"   
    return(g)
    
def check_index(row, prefix="Novel"):
    if "intersect" in row[-1]:
        out = prefix + "I"
    elif "closest" in row[-1] and "inside" not in row[-1]:
        out = prefix + "C"
    elif "inside" in row[-1]:
        out = prefix + "O"
    return(out)
    
def cut_gap(gap, threshold = 2000):
    if gap > threshold:
        gap = threshold
    return(gap)

# read each table and removed hits as csv
for table in tables:
    # read table
    with open(table, "r") as tab:
        reader = csv.reader(tab, delimiter='\t')
        table_tsv = [row for row in reader]
    
    # read hits
    with open(tablehits[table], "r") as tab:
        reader = csv.reader(tab, delimiter='\t')
        hits_tsv = [row for row in reader]
    
    # take hit's coords, order them and pick two from the middle
    for row in hits_tsv:
        # remove rows with the word 'unpaired'
        if "unpaired" in row[-1]:
            hits_tsv.remove(row)
        else:
            coords = [row[1], row[2], row[4], row[5]]
            coords.sort()
            gap = int(coords[2]) - int(coords[1])
            gap = cut_gap(gap)
            ori = check_gap(gap)
            index = check_index(row, prefix="")
            coords_to_table = ["regionX", ori] + [coords[1], str(int(coords[1])+100)] + [str(gap)] + [index] + row_to_add
            table_tsv.append(coords_to_table)
    
    name = table[:-4]+"2"+".txt"
    with open(name, "w") as out:
        writer = csv.writer(out, table_tsv, delimiter='\t')
        for row in table_tsv:
            writer.writerow(row)
            

            
            
            
