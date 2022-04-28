# ML-sklearning 自带数据
# 设置原始数据使用鸢尾花数据
import pandas as pd
from sklearn import datasets
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target


'''感知机'''
import matplotlib.pyplot as plt
import numpy as np
# 解决数据的二分问题的监督学习
# 样本数据
X = pd.DataFrame(iris_attr[:,2:],columns=['A1','A2'])
# 讲分类加入这个数据
X.insert(0,'class',iris_class)
# 由于是二分问题，所以之做2个种类的数据,由于是监督学习，因此必须要label
df = X[X['class'] != 2]
# 使用sklearn的感知机包进行学习
from sklearn.linear_model import Perceptron
X_train = df[['A1','A2']]
preceptron=Perceptron()
preceptron.fit(X_train,df['class'])
w = preceptron.coef_
b = preceptron.intercept_
print("感知器的分类准确度为：{:.2f}".format(preceptron.score(X_train,df['class'])))
#把图画出来
fig = plt.figure()
ax = fig.add_subplot()
plt.scatter(df[df['class']==0]['A1'],df[df['class']==0]['A2'], color="red",label="positive")
plt.scatter(df[df['class']==1]['A1'],df[df['class']==1]['A2'], color="green",label="negative")
line_x = np.arange(0,5,1)
line_y = -(line_x*w[0][0]+b[0])/w[0][1]
plt.plot(line_x,line_y)
plt.legend(loc="best")
plt.show()
# 应用方面：对具有某个特征的值进行分类
X_text=[[1.3,0.8],[0.6,1.2],[2.2,1.1]]
y=preceptron.predict(X_text)
print(y)


'''KNN'''
# 导入自带数据集（鸢尾花数据）
from sklearn import datasets
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target
# 导入sklearn中的KNN类
from sklearn.neighbors import KNeighborsClassifier
#########  以下为机器学习逻辑的基本流程  #######################
import numpy as np
# 设置随机种子，设置后每次调用该模块产生的随机数是一样的，不设置的话会按照系统时间作为参数
np.random.seed(0)
# 设置一个样本数据标签
indices = np.random.permutation(len(iris_attr))
# 随机选取数据标签中的140个作为训练集
x_train = iris_attr[indices[:-10]]
y_train = iris_class[indices[:-10]]
# 省下10个数据作为测试数据集
x_test = iris_attr[indices[-10:]]
y_test = iris_class[indices[-10:]]
# 训练数据
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
#预测数据
y_predict = knn.predict(x_test)
# 预测概率（有几个class就是几列，但排序要注意）
y_predict_prob=knn.predict_proba(x_test)

