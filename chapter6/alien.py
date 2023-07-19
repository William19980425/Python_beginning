#字典
alien_0 = {'color':'green','points':5}  # 键值对
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"你刚刚获得了{alien_0['points']}分")

print("====================================分割线====================================")
#为字典添加元素
print("添加元素前：")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("添加元素后：")
print(alien_0)

print("====================================分割线====================================")
#创建一个空字典
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 5
print(alien_0)

print("====================================分割线====================================")
#修改字典中的值
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

print("====================================分割线====================================")
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"初始位置是:{alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] =='medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"新位置是：{alien_0['x_position']}")

#删除键值对
print("====================================分割线====================================")
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
del alien_0['color']
print(alien_0)