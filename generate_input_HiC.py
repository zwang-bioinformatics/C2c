import numpy as np
import pickle 
import cooler
import math
import sys

#filepath2 = "../../shared/micro_C/mES_cool/mES_HiC_mm10_mapq30_1kb_2.6B.cool";
filepath2=sys.argv[1]
c2 = cooler.Cooler(filepath2)

res = sys.argv[2]
ch = int(sys.argv[3])
batch = []

for i in range(ch,ch+1):
	stc = "chr" + str(i)
	les = len(c2.bins().fetch(stc))
	sts = 0000
	leg = les*int(res)#length of chr
	ste = int(leg/1000000)*1000000
	#print(ste)

	#sts,ste = sts*int(res),ste*int(res)
	

	#print(les,sts,ste)
	stdif = (ste-sts)/(2400*int(res))
#	print(int(stdif))

	for j in range(int(stdif)):
		j0 = j*2400*int(res)
		j2 = j0+ 2400*int(res)
		sfe=stc+":"+str(j0)+"-"+str(j2)
		#print(sfe)

		mic1=c2.matrix(balance=True).fetch(sfe)
		#print(mic1.shape)

		for i1 in range(0,mic1.shape[0],200):
			for k in range(0,mic1.shape[0],200):
				#print(i1,k,sfe)

				m1 = mic1[i1:i1+200,k:k+200]
				m1[np.isnan(m1)]=0
				m1[m1>0.05]=0.05
				mic2=[]
				batch.append([m1])

with open(sys.argv[4],"wb") as file:
	pickle.dump(batch,file)
