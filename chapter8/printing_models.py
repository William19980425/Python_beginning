# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model:{current_design}")
#     completed_models.append(current_design)
# print("\nThe following models have been printed:")
# for completed in completed_models:
#     print(completed) 

def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止
       打印每个设计后,都将其移到列表completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("\nThe following models have been printed:")
    for completed in completed_models:
        print(completed.title())

#主程序
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# [:] 用切片表示法创建列表的副本,这样可以保留原来的未打印的设计列表； 比如： function_name(list_name[:])
print_models(unprinted_designs[:],completed_models)