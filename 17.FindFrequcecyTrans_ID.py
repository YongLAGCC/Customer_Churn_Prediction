#Author: Yong Zhou. NJIT. NSF
import pickle


dict={}
with open("/Users/yong.zhou/Dropbox/TranDetails.txt","rb") as pf:
    dict=pickle.load(pf)
    print(dict)

NumOfTrans={}
for key in dict:
    if key not in NumOfTrans:
        print(NumOfTrans[key].count(dict[key][0]))
        