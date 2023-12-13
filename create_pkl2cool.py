import pickle
import numpy as np
import sys
import math
import pandas as pd
import cooler

dtest = []
with open(sys.argv[1],"rb") as fh:
	dtest = pickle.load(fh)


binid1=[]
binid2= []
count=[]
df = pd.DataFrame(columns=["bin1_id","bin2_id","count"])
chrs=[]
st=[]
en=[]
we=[]
bs = pd.DataFrame(columns=["chrom","start","end","weight"])

c0 = 0

start = 0

for i in range(int(len(dtest)/144)):
	si = i * 144
	c=0
	lown = i * 2400000
	a0 = np.empty((0,0))
	for j in range(12):
		pi = si + j * 12
		a1 = np.array(dtest[int(pi)])
		a1 = a1.squeeze()
		for k in range(1,12):
			a2 = np.array(dtest[int(pi+k)])
			a2 = a2.squeeze()
			a1 = np.hstack((a1,a2))
		if j == 0:
			a0 = a1
		if j != 0:
			a0 = np.vstack((a0,a1))
			
	m = (10**(a0-1))/9*0.05
	start = i*2400
	for j in range(0,2400):
		a = (j+start)*1000
		b = a+1000
		chrs.append(str(sys.argv[2]))
		st.append(a)
		en.append(b)
		we.append(1.0)
		for k in range(j,2400):
			end1 = int(j+start)
			end2 = int(k+start)
			binid1.append(end1)
			binid2.append(end2)
			count.append(a0[j][k])
df["bin1_id"]=binid1
df["bin2_id"]=binid2
df["count"]=count
bs["chrom"]=chrs
bs["start"]=st
bs["end"]=en
bs["weight"]=we
cooler.create_cooler(cool_uri=sys.argv[3],bins=bs,pixels=df,dtypes={"count":"float64"})

