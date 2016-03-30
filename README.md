# structome
Toolbox development for structural variations within Irys data retrieved from the BioNano Genomics nick-labeling protocols.

# Input Files
In order to run most scripts you will need the following three files:

1. sample.xmap - The overall mapping flie with the columns: 
[XmapEntryID, QryContigID, RefContigID, QryStartPos, QryEndPos, RefStartPos, RefEndPos, Orientation, Confidence, HitEnum, QryLen, RefLen, LabelChannel, Alignment]

2. sample_r.cmap - The reference mapping file with the columns: 
[CMapId, ContigLength, NumSites, SiteID, LabelChannel, Position, StdDev, Coverage, Occurrence]

3. sample_q.cmap - The contig mapping file with the columnns: 
[CMapId, ContigLength, NumSites, SiteID, LabelChannel, Position, StdDev, Coverage, Occurrence, GmeanSNR, lnSNRsd, SNR]

# Usage
The code is writen in python using the following python packages: sys, linecache
Each file can be run off the command line.
# structomeIndel.py
Command Line
python structomeIndel.py Xmap_file Rcmap_file Qcmap_file Cutoff Output_file
Within Python
structomeIndel.py(Xmap_file, Rcmap_file, Qcmap_file, Cutoff, Output_file)
# structomeInversion.py
Command Line
structomeInversion.py Xmap_file Output_file
Within Python
structomeInversion.py(Xmap_file, Output_file)
#structome_repeats.py
Command Line
structome_repeats.py Xmap_file Qcmap_file Cutoff 
Within Python
structome_repeats.py(Xmap_file, Qcmap_file, Cutoff)
