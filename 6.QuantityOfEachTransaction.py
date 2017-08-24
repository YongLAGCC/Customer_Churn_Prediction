#AUTHOR YONG.ZHOU, NJIT, NSF
import pickle

dict_quantity={}

QUANTITY=0

p_file=open("/Users/yong.zhou/Desktop/supermarket/sale.csv")
p_line = p_file.readlines()

for line in p_line[1:]:
    attr=line.split(",")
    customer_id=attr[4]
    Qty=attr[5]

    if customer_id!= "NULL" and customer_id not in dict_quantity:
        dict_quantity[customer_id]=[]
    if customer_id!="NULL":
        dict_quantity[customer_id].append(Qty)


with open("/Users/yong.zhou/Dropbox/Yong/QuantityTransaction.txt","wb") as pf:
    pickle.dump(dict_quantity,pf)
    print(dict_quantity)
