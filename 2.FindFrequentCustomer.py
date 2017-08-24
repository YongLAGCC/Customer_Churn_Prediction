#Author: Yong Zhou. NJIT. NSF
import pickle


tran_dict={}
with open("/Users/yong.zhou/Dropbox/TranDetails.txt", "rb") as pf:
    tran_dict = pickle.load(pf)
    #print(tran_dict)



frequent_customer_list = []
for key in tran_dict.__iter__():
    if len(tran_dict[key][0]) >= 10:
        frequent_customer_list.append(key)
        #print(key, tran_dict[key][3],"++++++++")

with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","wb") as pf:
    pickle.dump(frequent_customer_list,pf)
    print(frequent_customer_list)
    print(len(frequent_customer_list))






# with open("/Users/yong.zhou/Dropbox/Yong/QuantityTransaction.txt","rb") as pf:
#     quantity_product=pickle.load(pf)
#     #print(quantity_product)
#
# frequent_custom_produst={}
#
# for key in quantity_product:
#     if key in frequent_customer_list:
#         print(quantity_product[key])

