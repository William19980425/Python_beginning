def great_user():
    """显示简单的问候语"""
    print("hello")

great_user()

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name}{last_name}"
    return full_name
#这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    l_name = input("Last name:")

    formatted_name = get_formatted_name(f_name,l_name)
    print("Your name is:"+formatted_name)