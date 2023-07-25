from pathlib import Path
import json


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        # contents = path.read_text()
        # print(contents)
        # username = json.loads(contents)
        print(f"Welcome back,{username}")
    else:
        # print("您查询的用户名不存在，请重新输入!")
        username = input("What is your name?\n")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back,{username}")
    
greet_user()

