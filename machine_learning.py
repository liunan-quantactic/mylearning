'''感知机'''
import matplotlib.pyplot as plt
import numpy as np
# 解决数据的二分问题的监督学习
# 设置原始数据：假如有n个点
fig = plt.figure()
ax = fig.add_subplot()
# 样本数据
x1 = [0,0.2,0.5,0.6,0.8,0.8,1.0,1,0.1,0.2,0.3,0.4,0,0.5]
x2 = [0,0.3,0.5,0.2,0.6,0.2,0.5,1,0.5,0.7,0.5,0.7,1,1]
# 标签(label监督学习一定要)
label = [0,0,0,0,0,0,0,0,1,1,1,1,1,1]
# 使用sklearn的包进行学习
from sklearn.linear_model import Perceptron
X_train = list(zip(x1,x2))
preceptron=Perceptron(n_iter=1000)
preceptron.fit(X_train,label)
w=preceptron.coef_
b=preceptron.intercept_
print("感知器的分类准确度为：{:.2f}".format(preceptron.score(X_train,label)))
plt.scatter(x1[0:8],x2[0:8], color="red",label="positive")
plt.scatter(x1[8:],x2[8:], color="green",label="negative")
line_x = np.arange(-0.1,1.5,0.1)
line_y = line_x*(-w[0][0]-b[0])/w[0][1]
plt.plot(line_x,line_y)
plt.legend(loc="best")
plt.show()

'''KNN'''
# 导入自带数据集（鸢尾花数据）
from sklearn import datasets
iris_attr = datasets.load_iris().data
iris_class = datasets.load_iris().target
