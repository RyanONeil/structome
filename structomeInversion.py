import sys, linecache
def main(Xmap_file, Output_file):
	with open(Xmap_file,'r') as Xmap, open(Output_file,'w') as output: 
		#output.write("Ref_ID\tContig_ID\tRef_Nick_ID\tContig_Nick_ID\tRef_Nick_prev_pos\tRef_Nick_pos\tContig_Nick_prev_pos\tContig_Nick_pos\tReff_diff\tContig_diff\tDiff_diff\tFLAG\tCoverage\n")
		first_match = True
		for Xline in Xmap:
			Xline = Xline.rstrip('\n')
			Xfield = Xline.split('\t')
			Xmatch = Xfield[-1].strip('(').rstrip(')').split(')(')
			if len(Xmatch) > 1:
				if first_match == True:
					X1 = Xfield[1]
					X2 = Xfield[2]
					X5 = Xfield[5]
					X6 = Xfield[6]
					first_match = False
				else:
					if Xfield[1] == X1 and Xfield[2] == X2:
						L1 = abs(int(round(float(X5)))-int(round(float(X6))))
						L2 = abs(int(round(float(Xfield[5])))-int(round(float(Xfield[6]))))
						if L1 <= L2:
							output.write(X2+"\t"+str(int(round(float(X5))))+"\t"+str(int(round(float((X6)))))+"\n")
						else: 
							output.write(Xfield[2]+"\t"+str(int(round(float(Xfield[5]))))+"\t"+str(int(round(float(Xfield[6]))))+"\n")
					X1 = Xfield[1]
					X2 = Xfield[2]
					X5 = Xfield[5]
					X6 = Xfield[6]
if __name__ == "__main__":
        if len(sys.argv) <3:
                sys.exit("usage: BioNano_Inversion.py(Xmap_file, Output_file) \n\
			Xmap_file: <run#>.xmap \n\
			Output_file: name of file to store output ")
	main(sys.argv[1],sys.argv[2])
