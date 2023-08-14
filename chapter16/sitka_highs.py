from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt

# path = Path('D:\A-professional\VScode\VScode-projects_python\example1\weather_data\sitka_weather_07-2021_simple.csv')
# 创建path对象接收csv文件
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# 读取csv文件,调用对象path的read_text方法，将数据赋给lines

lines = path.read_text().splitlines()
# 返回lines的类型，lines是一个列表
print(type(lines))
# 打印出lines的所有数据
# print(lines)

reader = csv.reader(lines)
print(f"reader的类型是:{type(reader)}")

# next方法返回文件中的下一行，因为是首次调用，所以返回的是文件的第一行,即表头
header_row = next(reader)
print(header_row)
header_row = next(reader)
print(header_row)

# enumerate()方法可以获取每个元素的索引及其值
for index,column_header in enumerate(header_row):
    print(index,column_header)

# 定义表头各项的list
years,monthes,days,levels = [],[],[],[]

# list不支持分片
# for row in reader[:10]:

# 提取日期(年+月+日)和等级
for row in reader:
    year = int(row[1])
    month = int(row[2])
    day = int(row[3])
    level = int(row[9])

    years.append(year)
    monthes.append(month)
    days.append(day)
    levels.append(level)
    print(f"{year}-{month}-{day}的等级是{level}")

# 绘图
# ctrl+shift+L可以选中一个变量，批量修改这个变量名
plt.style.use('seaborn')
fig,ax= plt.subplots()
ax.plot(levels,color='green')

# 设置图表的标题
ax.set_title("year",fontsize=25)
# 设置横坐标名称和字体大小
ax.set_xlabel('hengzuobiao',fontsize=16)
# 设置纵坐标名称和字体大小
ax.set_ylabel('zongzuobiao',fontsize=12)
# 
ax.tick_params(labelsize=6)

plt.show()

        