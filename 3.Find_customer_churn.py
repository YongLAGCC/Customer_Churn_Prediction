#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import pickle


tran_dict={}
with open("/Users/yong.zhou/Dropbox/TranDetails.txt", "rb") as pf:
    tran_dict = pickle.load(pf)
    #print(tran_dict)

frequent_customer_list = []
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customer_list=pickle.load(pf)
   # print(frequent_customer_list)

find_customer_churn={}
churn_num=0
stay_num=0
for key in tran_dict:
    if len(tran_dict[key][0]) >= 10:   # only the frequence customers

        len_date = 1486263618 - tran_dict[key][1][-1]
        len_date = len_date / 86400

        if len_date>=60 and key not in find_customer_churn:
            find_customer_churn[key]=(1)
            churn_num=churn_num+1

        elif len_date<60 and key not in find_customer_churn:
            find_customer_churn[key]=(0)
            stay_num=stay_num+1


with open("/Users/yong.zhou/Dropbox/FindCustomerChurn.txt","wb") as pf:
    pickle.dump(find_customer_churn,pf)
    print(find_customer_churn)
# print(len(find_customer_churn))
# print("Number of Customer who Churn: ",churn_num)
# print("Number of Customer who are stay: ",stay_num)





