import matplotlib.pyplot as plt

#折线图
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#点的横坐标
loss = [1.401, 0.871, 0.639, 0.415, 0.134, 0.0578, 0.0345,
        0.0370, 0.0355, 0.0328, 0.0287, 0.0249, 0.335, 0.335,
        0.336, 0.370, 0.0559, 0.0504, 0.0144, 0.0127]
top1_acc = [0.714,0.714,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1]
plt.plot(x,loss,'s-',color = 'r',label="Loss")#s-:方形
plt.plot(x,top1_acc,'o-',color = 'g',label="Top1_Acc")#o-:圆形
plt.xlabel("epochs")#横坐标名字
# plt.ylabel("accuracy")#纵坐标名字
plt.legend(loc = "best")#图例
plt.show()