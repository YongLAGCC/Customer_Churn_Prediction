#Author: Yong Zhou. NJIT. NSF
import pickle


amountOfEachCstomerTransUPC={}
with open("/Users/yong.zhou/Desktop/supermarket/amountOfEachCstomerTransUPC.txt.txt", "rb") as pf:
    amountOfEachCstomerTransUPC=pickle.load(pf)
    # print(amountOfEachCstomerTransUPC)
    # print(len(amountOfEachCstomerTransUPC))

frequent_customer_list=[]
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customer_list=pickle.load(pf)
    # print(frequent_customer_list)
    # print(len(frequent_customer_list))

loyalCustProduct_amount={}
for id in frequent_customer_list:
    if id not in loyalCustProduct_amount:
        loyalCustProduct_amount[id]={}
        if id in amountOfEachCstomerTransUPC:
            loyalCustProduct_amount[id]=amountOfEachCstomerTransUPC[id]





with open("/Users/yong.zhou/Desktop/supermarket/loyalCustProduct_amount.txt","wb") as pf:
    pickle.dump(loyalCustProduct_amount, pf)
    print(loyalCustProduct_amount)
    print(len(loyalCustProduct_amount))

