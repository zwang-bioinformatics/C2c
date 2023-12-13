import sys
import numpy as np
import pickle
import os
import datetime
from sklearn.metrics import matthews_corrcoef
from torch.utils import data
import torch
import torch.optim as optim
from torch.autograd import Variable
from time import gmtime, strftime
import torch.nn as nn
from torch.optim.lr_scheduler import ReduceLROnPlateau
import torch.nn.functional as F
import random
from operator import truediv

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import roc_auc_score
from sklearn.metrics import brier_score_loss
from sklearn.metrics import average_precision_score
from sklearn.metrics import confusion_matrix


from MicroCResNet import *

from torch_geometric.datasets import TUDataset
from torch_geometric.data import DataLoader

dtrain = []
with open(sys.argv[1], 'rb') as filehandle:
	dtrain = pickle.load(filehandle)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = CustomResNet().to(device)
model.load_state_dict(torch.load(sys.argv[2]))

model.eval()

batchs = []
for batch in dtrain:
	hic = Variable(torch.from_numpy(np.array(batch[0]))).to(device,dtype=torch.float)
	hic = torch.unsqueeze(torch.unsqueeze(hic,0),0)
	out2 = model(hic)
	out2 = out2.cpu().data.numpy()
	batchs.append([out2])
import pickle
with open(sys.argv[3],"wb") as fp:
	pickle.dump(batchs,fp)	
