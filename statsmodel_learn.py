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
#mod = smf.Probit(endog,exog).fit()
mod.summary()
# 预测结果
y_predict = mod.predict(df[['A1','A2']].iloc[indices[90:]])
result = pd.concat([y_predict,df['class'].iloc[indices[90:]]],axis=1)

# 使用机器学习的logisticregression
from sklearn import linear_model as lm
result = lm.LogisticRegression().fit(exog.values,endog.values)


'''分位数回归
解决数据有离群点时的参数显著性问题,按照被解释变量进行分位数排序
相关方式可以对自变量进行分段：有门槛回归（没有明显分段，用于找断点），断点回归（明显断点上面看是否存在变化）
'''

'''辅助工具可以用qqplot确定数据是否是正态分布（也可以选择其他分布形式）'''
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
df = sm.datasets.engel.load_pandas().data
ax = plt.subplot(111)
sm.qqplot(df['foodexp'],fit=True,line='45')#qqplot
mod = smf.quantreg('foodexp~income',df).fit(q=0.5)
mod.summary()

'''聚类稳健标准误的回归
由于同一个个体在不同时期扰动项之间村来自相关，因此使用聚类稳健标准误，同一个聚类观测值允许存在相关性可以对fit()中的cov_type参数进行修改'''


'''朴素贝叶斯 还是二分问题'''
from sklearn import datasets
import pandas as pd
import numpy as np
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target
from sklearn.naive_bayes import GaussianNB,MultinomialNB  #高斯朴素贝叶斯和多项朴素贝叶斯
'''高斯朴素贝叶斯和多项朴素贝叶斯结果可能不同，取决于选择了哪一种分布函数'''
gnb = GaussianNB()
gnb = MultinomialNB()
y_pred = gnb.fit(iris_attr, iris_class)
#分类取值的概率
X=[[6.3,4,6.4,1]]
y_pred.predict(X)
y_pred.predict_proba(X)