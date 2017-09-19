#Author: Yong Zhou. NJIT. NSF
import datetime as DT
import math
import pickle
DATE=1

DifferDate={}
averageDatePurchase={}
squareDiffer = {}


def main():

    with open("/Users/yong.zhou/Dropbox/TranDetails.txt","rb") as pf:
        dict=pickle.load(pf)

    print(averageOfDATE(dict))

    print(AverageOfDifferDay(DifferDate))
    print(DifferOfSquare(averageDatePurchase,DifferDate))


def averageOfDATE(dict):

    for key in dict:
        Interval_dates = 0
        if key not in DifferDate and len(dict[key][DATE])>=10:
            DifferDate[key]=[]
            for date in dict[key][DATE]:
                index= dict[key][DATE].index(date)
                if (index+1)!=len(dict[key][DATE]):
                    Interval_dates=abs(float(dict[key][DATE][index+1])-float(date))
                    DifferDate[key].append(Interval_dates)
    return DifferDate

def AverageOfDifferDay(DifferDate):

    for key in DifferDate:
        if key not in averageDatePurchase:
            averageDatePurchase[key]=[]
            sum=0
            for differ in DifferDate[key]:
                sum=sum+float(differ)
            sum=(sum/(len(DifferDate[key]))-1)
            averageDatePurchase[key]=sum

    return averageDatePurchase


def DifferOfSquare(averageDatePurchase,DifferDate):
    for key in averageDatePurchase:
        if key not in squareDiffer:
            squareDiffer[key]=""
            sum=0

            #for average in averageDatePurchase[key]:
            if key in DifferDate:
                for date in DifferDate[key]:
                    sum=sum+(float(averageDatePurchase[key])-float(date))**2
                sum=sum/len(DifferDate[key])
                sum=math.sqrt(sum)
                squareDiffer[key]=sum
    return squareDiffer
                        
        


main()