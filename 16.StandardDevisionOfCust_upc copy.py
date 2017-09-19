#Author: Yong Zhou. NJIT. NSF
import pickle

average_upc_PerID={}
with open("/Users/yong.zhou/Desktop/supermarket/average_upc_PerID.txt","rb") as pf:
    average_upc_PerID=pickle.load(pf)
    print(average_upc_PerID)
    print(len(average_upc_PerID))
