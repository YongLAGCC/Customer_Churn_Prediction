# #Author: Yong Zhou. NJIT. NSF
import pickle

amountOfEachCstomerTransUPC={}
with open("/Users/yong.zhou/Desktop/supermarket/amountOfEachCstomerTransUPC.txt.txt", "rb") as pf:
    amountOfEachCstomerTransUPC=pickle.load(pf)
    print(amountOfEachCstomerTransUPC)


TotalUpcNumber=[]
with open("/Users/yong.zhou/Dropbox/TotalUPCnumber.txt","rb") as pf:
    TotalUpcNumber=pickle.load(pf)


frequent_customer_dict={}
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customer_dict=pickle.load(pf)

# customer_churn_dict={}
# with open("/Users/yong.zhou/Dropbox/FindCustomerChurn.txt","rb") as pf:
#     customer_churn_dict=pickle.load(pf)




dictionary={}
with open("/Users/yong.zhou/Desktop/supermarket/10.ProductsPerCustomer.txt","wb") as pf:
    for pid in frequent_customer_dict:
        if pid not in dictionary:

            line = pid + ","
            for upc in TotalUpcNumber:
                if (pid in amountOfEachCstomerTransUPC):
                    if (upc in amountOfEachCstomerTransUPC[pid]):
                        line = line + str(amountOfEachCstomerTransUPC[pid][upc]) + ","
                    else:
                        line = line + "0,"
                else:
                    line = line + "0,"
            dictionary[pid] = [line]
            #list.append(line + str(customer_churn_dict[pid]))
            #print(line + str(customer_churn_dict[pid]))
            #pickle.dump(line+str(customer_churn_dict[pid]),pf)


# print(list)



with open("/Users/yong.zhou/Desktop/supermarket/ProductsPerCustomerCopy.10.txt","wb") as pf:
    pickle.dump(dictionary,pf)
    print(dictionary)
    print(len(dictionary))



