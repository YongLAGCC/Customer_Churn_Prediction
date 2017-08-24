#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import pickle

p_file=open("/Users/yong.zhou/Desktop/supermarket/sale.csv")
p_line = p_file.readlines()

dictionary={}
TRANS=0
DATE=1
PRICE=2
PRODUCT=3
QTY=4
for line in p_line[1:]:
    attribute=line.split(',')
    Date=attribute[0];TransactionNumber=attribute[1];UPCNumber=attribute[2]
    ProductName=attribute[3]; CustomerAccount=attribute[4]; Qty=attribute[5]
    RegularPrice=attribute[6]; SalePrice=attribute[7]
    trans_price=float(Qty)*float(SalePrice)

    if CustomerAccount!="NULL" and not dictionary.__contains__(CustomerAccount):
        dictionary[CustomerAccount]=[[],[],[],[],[]]

    if CustomerAccount!="NULL" and not TransactionNumber in dictionary[CustomerAccount][TRANS]:

        dictionary[CustomerAccount][TRANS].append(TransactionNumber)

        finaltime = DT.datetime.strptime(Date, "%Y-%m-%d %H:%M:%S.%f")
        finalT = int(finaltime.strftime('%s'))

        dictionary[CustomerAccount][DATE].append(finalT)
        dictionary[CustomerAccount][PRICE].append([])
       # dictionary[CustomerAccount][PRODUCT].append([])
        #dict[CustomerAccount][QTY].append([])



    if CustomerAccount!="NULL"\
            and not trans_price in dictionary[CustomerAccount][PRICE]\
            and not ProductName in dictionary[CustomerAccount][PRODUCT]:

         dictionary[CustomerAccount][PRICE][-1].append(trans_price)
         dictionary[CustomerAccount][PRODUCT].append(UPCNumber)
         dictionary[CustomerAccount][QTY].append(Qty)


p_file.close()



# for key in dictionary.__iter__():
#     print(key, ": ", dictionary[key])
#


dict={}
dict=dictionary.copy()

for key in dict:
    for price_list in dict[key][PRICE]:
        sum=0
        index =0
        for price in price_list:
            sum=sum+price
        index=dict[key][PRICE].index(price_list)
        dict[key][PRICE][index]=sum
    #print(dict)

with open("/Users/yong.zhou/Dropbox/TranDetails.txt","wb") as pf:
    pickle.dump(dict,pf)
    print(dict)




