'''Do all without having to retype'''
#from CSV import imp
import pandas as pd
import numpy as np
from StringToDateTime import StringToDateTime as STD
from QuickView import QuickView as QW

file_path    = 'C:\\Users\\212410226\\Workspace\\GE Projects\\Skorpion Zinc\\BLUEPRINT\\'
file_name    = '7.1 BlueprintOutput(2014).csv'
file_name    = '2. DATA Interpolated Free acid added(First_Couple_of_months).csv'
#Raw_Data     = imp(file_path+file_name,0)
#Header       = np.array(Raw_Data[0][1:])
#DateTime     = np.array(STD(np.array(Raw_Data[1])[:100000,0],1))
#Data         = np.array(np.array(Raw_Data[1])[:100000,1:]).astype(np.float)


df           = pd.read_csv(file_path + file_name)
DateTime     = np.array(STD(df.Timestamp,1))
df.Timestamp = DateTime

Header       = df.columns.values[1:]
Data         = df.iloc[:,1:].values
A            = QW(Header,DateTime,Data)





#mask = Data[:,36] > 0.1
#Data = Data[mask,:]
#DateTime = DateTime[mask]
#A.get_fields_and_stats(30)

#A.multi_scatter(19,[36, 21, 24, 27, 30, 33], 1, 6)
#A.single_scatter(19, [33, 30])
#A.multi_hist([36, 21, 24, 27, 30, 33], 1, 6)




#min_pH             =  1.5
#max_pH             =  2.5
#min_pH_Slope       = -0.005
#max_pH_Slope       = 0.005
#min_Temp           =  45.0
#max_Temp           =  60.0
#min_Temp_Slope     = -0.05
#max_Temp_Slope     =  0.05  
#min_Density        =   1.0
#max_Density	        =  1.6
#min_SlurFeed	  =  50.0
#max_SlurFeed	  =  1000.0
#min_RafFeed	       =  100.0
#max_RafFeed	       =  2000.0
#
#mask               = (  (Data[:,0] > min_Density)  & 
#                        (Data[:,0] < max_Density)  &
#                        (Data[:,2] > min_SlurFeed) &
#                        (Data[:,2] < max_SlurFeed) &
#                        (Data[:,3] > min_RafFeed)  &
#                        (Data[:,3] < max_RafFeed)  
#                     )