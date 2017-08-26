# #Author: Yong Zhou. NJIT. NSF
import pickle

amountOfEachCstomerTransUPC={}
with open("/Users/yong.zhou/Desktop/supermarket/amountOfEachCstomerTransUPC.txt.txt", "rb") as pf:
    amountOfEachCstomerTransUPC=pickle.load(pf)



TotalUpcNumber=[]
with open("/Users/yong.zhou/Dropbox/TotalUPCnumber.txt","rb") as pf:
    TotalUpcNumber=pickle.load(pf)
    print(TotalUpcNumber)


frequent_customer_dict={}
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    frequent_customer_dict=pickle.load(pf)


customer_churn_dict={}
with open("/Users/yong.zhou/Dropbox/FindCustomerChurn.txt","rb") as pf:
    customer_churn_dict=pickle.load(pf)




line_key={}
# print(len(TotalUpcNumber))
# print(type(amountOfEachCstomerTransUPC))

first_line="Customer_ID,"
for upc in TotalUpcNumber:
    first_line=first_line+upc+","
print(first_line,"Customer_Churn_Or_Not")


line=[]
with open("/Users/yong.zhou/Desktop/supermarket/10.ProductsPerCustomer.txt","wb") as pf:
    for pid in frequent_customer_dict:
        line = pid + ","
        for upc in TotalUpcNumber:
            if (pid in amountOfEachCstomerTransUPC):
                if (upc in amountOfEachCstomerTransUPC[pid]):
                    line = line + str(amountOfEachCstomerTransUPC[pid][upc]) + ","
                else:
                    line = line + "0,"
            else:
                line = line + "0,"


        print(line + str(customer_churn_dict[pid]))
        pickle.dump(line+str(customer_churn_dict[pid]),pf)


with open("/Users/yong.zhou/Desktop/supermarket/10.ProductsPerCustomer.txt","rb") as pf:
    line1=pickle.load(pf)


























comment='''


def count(index, i):
    if i == index and len(line_key[key]) - 1 >= index:
        return amountOfEachCstomerTransUPC[key][upcNumber]
    if i == index:
        return amountOfEachCstomerTransUPC[key][upcNumber]
    elif len(line_key) - 1 >= i:
        pass
    else:
        return 0

for key in amountOfEachCstomerTransUPC:
    if key in frequent_customer_list and key not in line_key:
        line_key[key]=[]
        print(len(TotalUpcNumber))
        for upcNumber in filter(lambda x: x in TotalUpcNumber,amountOfEachCstomerTransUPC[key]):
            index=TotalUpcNumber.index(upcNumber)
            line_key[key] = list(map(lambda x: count(index, x), range(0,len(TotalUpcNumber))))
            # for i in :
                # if i == index and len(line_key[key])-1 >=index:
                #     line_key[key][index] = amountOfEachCstomerTransUPC[key][upcNumber]
                # if i == index:
                #     line_key[key].append(amountOfEachCstomerTransUPC[key][upcNumber])
                # elif len(line_key)-1 >=i:
                #     continue
                # else:
                #     line_key[key].append(0)
            # print(line_key[key])
        # for upc in TotalUpcNumber:
        #     line = line +" "+amountOfEachCstomerTransUPC[key][upc]
        #     print(line_key)

print(line_key)

'''







