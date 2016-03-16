import sys, linecache, string
def main(Xmap_file, Rcmap_file, Qcmap_file, Cutoff, Output_file):
	with open(Xmap_file,'r') as Xmap, open(Output_file,'w') as output: 
		output.write("Ref_ID\tContig_ID\tRef_Nick_ID\tContig_Nick_ID\tRef_Nick_prev_pos\tRef_Nick_pos\tContig_Nick_prev_pos\tContig_Nick_pos\tReff_diff\tContig_diff\tDiff_diff\tFLAG\tCoverage\n")
		for Xline in Xmap:
			first_match = True
			Xline = Xline.rstrip('\n')
			Xfield = Xline.split('\t')
			Xmatch = Xfield[-1].strip('(').rstrip(')').split(')(')
			if len(Xmatch) > 1:
				Ref_ID = Xfield[2]
				Contig_ID = Xfield[1]
				for Rnum, Rline in enumerate(open(Rcmap_file)):
					Rfield = Rline.split('\t')
					try:
						int(Rfield[0])
						if int(Rfield[0]) == int(Ref_ID):
							Rindex = Rnum
							break
					except ValueError: continue

				for Qnum, Qline in enumerate(open(Qcmap_file)):
					Qfield = Qline.split('\t')
					try:
						int(Qfield[0])	
						if int(Qfield[0]) == int(Contig_ID):
							Qindex = Qnum
							break
					except ValueError: continue

				for match in Xmatch:
					match = match.split(',')
					Rmatch = match[0]
					Rpos = str(int(round(float(linecache.getline(Rcmap_file,int(Rindex)+int(Rmatch)).split('\t')[5]))))
					Qmatch = match[1]
					Qpos = str(int(round(float(linecache.getline(Qcmap_file,int(Qindex)+int(Qmatch)).split('\t')[5]))))
					Coverage = linecache.getline(Qcmap_file,int(Qindex)+int(Qmatch)).split('\t')[7]
					if first_match:
						R_prev = Rpos
						Q_prev = Qpos
						output.write(Ref_ID+"\t"+Contig_ID+"\t"+Rmatch+"\t"+Qmatch+"\t"+Rpos+"\t"+Rpos+"\t"+Qpos+"\t"+Qpos+"\t0\t0\t0\tMATCH\t"+Coverage+"\n")
						first_match = False
					else:
						R_diff = abs(int(Rpos) - int(R_prev))
						Q_diff = abs(int(Qpos) - int(Q_prev))
						Diff_diff = abs(R_diff-Q_diff)
						if Diff_diff >= int(Cutoff):
							if R_diff - Q_diff > 0: flag = 'DEL'
							if R_diff - Q_diff < 0: flag = 'IN'
							if R_diff - Q_diff == 0: flag = 'MATCH'
						else: flag = 'MATCH'
						output.write(Ref_ID+"\t"+Contig_ID+"\t"+Rmatch+"\t"+Qmatch+"\t"+R_prev+"\t"+Rpos+"\t"+Q_prev+"\t"+Qpos+"\t"+str(abs(R_diff))+"\t"+str(Q_diff)+"\t"+str(Diff_diff)+"\t"+flag+"\t"+Coverage+"\n")
						R_prev = Rpos
						Q_prev = Qpos	

if __name__ == "__main__":
        if len(sys.argv) <6:
                sys.exit("usage: BioNano_Indel.py(Xmap_file, Rcmap_file, Qcmap_file, Cutoff, Output_file) \n\
			Xmap_file: <run#>.xmap \n\
			Rcmap_file: <run#>_r.cmap \n\
			Qcmap_file: <run#>_q.cmap \n\
			Cutoff: size needed to justify InDel \n\
			Output_file: name of file to store output ")
	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
