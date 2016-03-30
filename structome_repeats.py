import sys, linecache, string
def main(Xmap_file, Qcmap_file, Cutoff):
	Q_set = []
	Q_prev = 0
	for Qline in open(Qcmap_file):
		Qfield = Qline.split('\t')
		try: 
			int(Qfield[0])
			if Q_prev != int(Qfield[0]):
				Q_set.append(int(Qfield[0]))
				Q_prev = int(Qfield[0])		
		except ValueError: continue


	for Xline in open(Xmap_file):
		Xline = Xline.rstrip('\n')
		Xfield = Xline.split('\t')
		try:
			int(Xfield[1])
			if int(Xfield[1]) in Q_set and float(Xfield[8]) >= float(Cutoff):
 				Q_set.remove(int(Xfield[1]))
		except ValueError: continue
		except IndexError: continue
	Q_set.sort()		
	for Q in Q_set:
		print Q
			
if __name__ == "__main__":
        if len(sys.argv) <4:
                sys.exit("usage: structome_repeats.py(Xmap_file, Qcmap_file, Cutoff) \n\
			Xmap_file: <run#>.xmap \n\
			Rcmap_file: <run#>_r.cmap \n\
			Qcmap_file: <run#>_q.cmap \n\
			Cutoff: Confidence Cutoff")
	main(sys.argv[1],sys.argv[2],sys.argv[3])
