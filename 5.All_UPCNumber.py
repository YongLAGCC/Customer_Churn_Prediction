#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import pickle


frequent_customerID_list = []
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customerID_list=pickle.load(pf)
    # print(frequent_customerID_list)
    # print(len(frequent_customerID_list))
    # print("++++++")



p_file=open("/Users/yong.zhou/Desktop/supermarket/sale.csv")
p_line = p_file.readlines()

dictionary={}
TRANS=0
DATE=1
CUSTOMER_ACCOUNT=4

UPCNUM=[]
for line in p_line:
    attri=line.split(",")
    upcNumber= attri[2]
                                 # ONLY the ID of FREQUENCE CUSTOMERS
    for frequent_customer_ID in frequent_customerID_list:
        if attri[CUSTOMER_ACCOUNT] !="NULL" \
                and frequent_customer_ID in attri[CUSTOMER_ACCOUNT] and upcNumber not in UPCNUM:
            UPCNUM.append(upcNumber)
print(UPCNUM)

p_file.close()

with open("/Users/yong.zhou/Dropbox/TotalUPCnumber.txt", 'wb') as pf:
    pickle.dump(UPCNUM, pf)
    print(UPCNUM)
    print(len(UPCNUM))



