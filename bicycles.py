bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print("====================================分割线====================================")
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

print("====================================分割线====================================")
#索引指定为-1可让Python返回最后一个列表元素，在不知道列表长度的情况下很好用
print(bicycles[-1])

print("====================================分割线====================================")
message = f"My first bicycle was a {bicycles[2].title()}"
print(message)

