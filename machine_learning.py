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
# 使用sklearn的包进行学习
from sklearn.linear_model import Perceptron
X_train = df[['A1','A2']]
preceptron=Perceptron()
preceptron.fit(X_train,df['class'])
w=preceptron.coef_
b=preceptron.intercept_
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

'''KNN'''
# 导入自带数据集（鸢尾花数据）
from sklearn import datasets
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target
