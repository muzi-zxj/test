import pandas as pd
import numpy as np
from pyEDM import *
import pyEDM
data=np.load("H:\\Dataset\\MDD\\stand\\channel_order\\S1_test_x.npy")
new_data = data.swapaxes(1, 2)
col=new_data[0,:,0]
tar=new_data[0,:,8]
time_index = np.arange(1, 513)
df = pd.DataFrame({'time':time_index,'col': col, 'tar': tar})
print(df)
sardine_anchovy_sst = sampleData['sardine_anchovy_sst']
# print(sardine_anchovy_sst.shape)
print(sardine_anchovy_sst)
# sardine_anchovy_sst[['anchovy','np_sst']].plot()
df[['col','tar']].plot()
CCM( dataFrame = df, E = 3,tau=1, libSizes = "10 500 50",
     columns = "col", target = "tar", sample = 100, showPlot = True )