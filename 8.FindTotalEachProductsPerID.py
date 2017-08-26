import pickle

#
# frequent_customer_list={}
# with open("/Users/yong.zhou/Dropbox/Yong/frequentCustomerUpcNumbers.txt","rb") as pf:
#     frequent_customer_list=pickle.load(pf)
#     #print(frequent_customer_list)



dictionaryOfFrequentCust={}
with open("/Users/yong.zhou/Dropbox/Yong/FrequentCustomerDictionary.txt","rb") as pf:
    dictionaryOfFrequentCust=pickle.load(pf)
    print(dictionaryOfFrequentCust)

quantity_upc={}
with open("/Users/yong.zhou/Dropbox/Yong/QuantityTransaction.txt",'rb') as pf:
    quantity_upc=pickle.load(pf)
    print(quantity_upc)


