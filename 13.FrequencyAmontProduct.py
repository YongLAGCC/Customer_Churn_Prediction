#Author: Yong Zhou. NJIT. NSF
import pickle


frequency_customer_churn=[]
with open("/Users/yong.zhou/Dropbox/FindCustomerChurn.txt","rb") as pf:
    frequency_customer_churn=pickle.load(pf)
    #print(frequency_customer_churn)

weeklyProductPerId=[]
with open("/Users/yong.zhou/Desktop/supermarket/ProductsPerIDWeekly.13.txt","rb") as pf:
    weeklyProductPerId=pickle.load(pf)


TotalUpcNumber=[]
with open("/Users/yong.zhou/Dropbox/TotalUPCnumber.txt","rb") as pf:
    TotalUpcNumber=pickle.load(pf)

totalupc=[]
totalupc.append('CUSTOMER_ID')
for upcNumber in TotalUpcNumber:
    totalupc.append(upcNumber)
totalupc.append('CHURN_Or_Not')
print(totalupc)

average_weekly_product={}

with open("/Users/yong.zhou/Desktop/supermarket/average_weekly_product.13.txt","wb") as pf:
    for key in frequency_customer_churn:
        if key in weeklyProductPerId and key not in average_weekly_product:
            average_weekly_product[key]=[]
            for quantity in weeklyProductPerId[key]:
                if quantity !=key:
                    average_weekly_product[key].append(quantity)

            average_weekly_product[key].append(frequency_customer_churn[key])

    print(average_weekly_product)
    pickle.dump(average_weekly_product,pf)
