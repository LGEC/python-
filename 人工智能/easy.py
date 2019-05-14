from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

#生成-1到200均匀分布的数字
x=np.linspace(-1,1,200)
np.randow.shuffle(x)

#利用x生成y，并随机加入0.05之内的扰动
y=0.5*x+2+np.randow.normal(0,0.05,(200,))

plt.scatter(x,y)
plt.show()

#截取160个数据作为训练数据
# 截取40个数据作为测试数据
x_train = x[:160]
x_test = x[160:]
y_train = y[:160]
y_test = y[160:]

# 新建一个流式网络
model = Sequential()

# 增加一个全连接层，输入一个参数，输出一个参数
model.add(Dense(output_dim=1,input_dim=1))

# 编译网络，损失函数mse，优化函数sgd
model.compile(lose='mse',optimizer='sgd')

# 训练301次
for step in range(500):
    cost = model.train_on_batch(x_train,y_train)

    # 每100次打印一次损失
    if step%100==0:
        print("cost:",cost)

# 使用测试数据，测试流失
cost = model.evaluate(x_test,y_test,batch_size=40)
print("test cost:",cost)

# 获取第一层网络的权重
w,b = model.layers[0].get_weights()
print("w:",w,"b:",b)

# 画图展示训练结果
y_pred = model.predict(x_test)
plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred)

plt.show()