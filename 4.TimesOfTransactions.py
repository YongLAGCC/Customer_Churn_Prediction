#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import pickle


tran_dict={}
with open("/Users/yong.zhou/Dropbox/TranDetails.txt", "rb") as pf:
    tran_dict = pickle.load(pf)
    #print()


with open("/Users/yong.zhou/Dropbox/TotalUPCnumber.txt", "rb") as pf:
    upcnumbers= pickle.load(pf)
    #print(upcnumbers)

#
# with open("/Users/yong.zhou/Dropbox/Yong/QuantityTransaction.txt","rb") as pf:
#     quantity_product=pickle.load(pf)
#     #print(quantity_product)


keys=[]
with open("/Users/yong.zhou/Dropbox/FrequentCustomerList.txt","rb") as pf:
    keys=pickle.load(pf)
    #print(keys)

# tran_dict={}
# with open("/Users/yong.zhou/Dropbox/Yong/frequentCustomerUpcNumbers.txt","rb") as pf:
#     tran_dict=pickle.load(pf)

times_transactions_dict = {}
for key in keys[:2]:
    if key not in times_transactions_dict:
        times_transactions_dict[key] = []
        for products_number in tran_dict[key][3]: # only keys and upc numbers
            for products_number in upcnumbers:

                index = upcnumbers.index(products_number)

                for i in range(0, len(upcnumbers)) and len:
                    if i == index and len(times_transactions_dict[key])-1>=index:
                        try:
                            times_transactions_dict[key][index] += tran_dict[key][5]
                        except IndexError as e:
                            times_transactions_dict[key].append(1)
                    elif i > len(times_transactions_dict[key])-1:
                        times_transactions_dict[key].append(0)

                    else:
                        times_transactions_dict[key][i] = times_transactions_dict[key][i]


for key in sorted(times_transactions_dict.__iter__()):
    print(key,": ", times_transactions_dict[key])

with open("/Users/yong.zhou/Dropbox/Yong/TimesOfUpc.txt","wb") as pf:
    pickle.dump(times_transactions_dict, pf)






