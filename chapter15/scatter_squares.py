import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

ax.axis([0,1100,0,110_0000]) #设置每个坐标轴的取值范围
# ax.ticklabel_format(style='plain') #设置matplotlib始终使用常规表示法
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=5)
ax.set_title("Square Nmubers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)
ax.tick_params(labelsize=14)

"""
    plt.show()
    plt.savefig('squares_plot.png',bbox_inches='tight')
    使用plt.savefig()保存生成的图片时,打开生成的图片是一片空白
    在 plt.show()后调用了plt.savefig(),在plt.show()后实际上已经创建了一个新的空白的图片，
    这时候再plt.savefig()就会保存这个新生成的空白图片
    解决方案: 把plt.savefig()放到plt.show()前面即可
    libpng warning: iCCP: cHRM chunk does not match sRGB
    出现这种警告的原因居然和输入法有关，把输入法切换成系统自带的就没有警告了 
"""
plt.savefig('squares_plot.jpg',bbox_inches='tight')
plt.show()