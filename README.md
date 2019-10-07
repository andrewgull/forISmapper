Script for processing [ISmapper](https://github.com/jhawkey/IS_mapper) output files (slightly modified version of 
[this](https://github.com/aurbn/IS_mapper/blob/master/scripts/compiled_table.py) script)
We modified the script **compiled_table.py** in order to keep all the hits considered by ISMapper as inaccurate. 
Here an alternative method for merging hits is used: to be merged an intersection of ranges or both ends of new hit 
should be placed within tolerance (default, -1 b.p.) from any existing hit. 
All additional inaccurate hits being marked either as “closest”, “intersect” or “inside the other” depending on 
what bed file they came from.


Procedure or workflow:

1. run_ISmap_batch.py
2. AppendRemovedHits2.py
3. compiled_table3.py

**NB:** all these scripts were designed for older version of IS_mapper which uses samtools v0.1.18 or v0.1.19
(**not** v1.9), and BedTools v2.17.0