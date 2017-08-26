import pandas as pd
import sklearn.linear_model as skl_lm
import sklearn as skl

mydata=pd.read_csv("/Users/yong.zhou/Dropbox/Yong/Yong.csv")
mydata.dtypes

mydata=pd.get_dummies(mydata)
mydata.dtypes

# print(mydata)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
predictor_var = list(mydata)[:-2]
target_var = list(mydata)[-1]

import sklearn.linear_model as skl_lm
model = skl_lm.LogisticRegression()
model.fit(mydata[predictor_var],mydata[target_var])

print(model)

import sklearn as skl
predictions = model.predict(mydata[predictor_var])
accuracy=skl.metrics.accuracy_score(predictions, mydata[target_var])

print(predictions)
print(accuracy)






print("Cross-validation ++++++++++++++++++++++++++")

predictor_var = list(mydata)[:-2]
target_var = list(mydata)[-1]
#
# import sklearn.tree as skl_tr
# model = skl_tr.DecisionTreeClassifier()

import sklearn.model_selection as skl_ms
scores = skl_ms.cross_val_score(model, mydata[predictor_var],mydata[target_var], cv=5)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
