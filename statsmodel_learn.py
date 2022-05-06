'''逻辑回归
该问题主要是解决二分问题，可以选择的方法有感知器，逻辑回归'''
import statsmodels.api as sm
from statsmodels.discrete.discrete_model import Logit, Probit, MNLogit
# 由于是二分问题，使用机器学习库中鸢尾花的数据
from sklearn import datasets
import pandas as pd
import numpy as np
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target
# 样本数据
X = pd.DataFrame(iris_attr[:,2:],columns=['A1','A2'])
# 讲分类加入这个数据
X.insert(0,'class',iris_class)
# 由于是二分问题，所以之做2个种类的数据,由于是监督学习，因此必须要label
df = X[X['class'] != 2]
# 打乱顺序
np.random.seed(0)
indices = np.random.permutation(len(df))
df = X[X['class'] != 2]
endog = df['class'].iloc[indices[0:90]]
exog = df[['A1','A2']].iloc[indices[0:90]]
# 进行逻辑回归的分析
#logit或者probit方法
mod = sm.Logit(endog,exog).fit()
#mod = sm.Probit(endog,exog).fit()
mod.summary()
# 预测结果
y_predict = mod.predict(df[['A1','A2']].iloc[indices[90:]])
result = pd.concat([y_predict,df['class'].iloc[indices[90:]]],axis=1)

# 使用机器学习的logisticregression
from sklearn import linear_model as lm
result = lm.LogisticRegression().fit(exog.values,endog.values)


