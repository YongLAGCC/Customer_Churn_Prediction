#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import pickle



frequent_customer_list = []
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customer_list=pickle.load(pf)


keys=[]
for customer in frequent_customer_list:
    keys.append(customer)

with open("/Users/yong.zhou/Dropbox/Yong/keysOfFrequenceCustomers.txt","wb") as pf:
    pickle.dump(keys,pf)
    print(keys)
    print(len(keys))