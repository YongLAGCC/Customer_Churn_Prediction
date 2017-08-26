#Author: Yong Zhou. NJIT. NSF

import pickle

transDetails={}
trans_inWeek=[]
with open("/Users/yong.zhou/Dropbox/TranDetails.txt","rb") as pf:
    transDetails=pickle.load(pf)
    #print(transDetails)
    index=0
for key in sorted(transDetails.__iter__()):
    if len(transDetails[key][1])>=10:
        trans_inWeek.append([key])
        index=trans_inWeek.index([key])
        tran_interval=((transDetails[key][1][-1]-(transDetails[key][1][0]))/604800)
        trans_inWeek[index].append(tran_interval)
print(trans_inWeek)
print(len(trans_inWeek))

with open("/Users/yong.zhou/Dropbox/transFrequencyInWeek.txt","wb") as pf:
    pickle.dump(trans_inWeek,pf)


