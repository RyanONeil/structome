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

# Outputs
Here is a list of all the outputs by column:

Ref_ID = RefContigID obtained from the Xmap file

Contig_ID = QryContigID obtained from the Xmap file

Ref_Nick_ID = ID number for Rcmap file

Contig_Nick_ID = ID number for Qcmap file

Ref_Nick_prev_pos = Rcmap start position

Ref_Nick_pos = Rcmap end position

Contig_Nick_prev_pos = Qcmap start position

Contig_Nick_pos = Qcmap end position

Reff_diff = Length of Rcmap

Contig_diff = Length of Qcmap

Diff_diff = Difference between Rcmap and Qcmap

FLAG = Label of insertion or deletion

Coverage = Read coverage from the Qcmap file
