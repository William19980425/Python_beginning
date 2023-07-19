banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()},你可以回复")

print("====================================分割线====================================")
ages = [11,15,3,7,19,18,62,52]
for age in ages:
    if age < 4:
        print(f"你是{age}岁,你可以半价购买票")
    elif age < 60:
        print(f"你是{age}岁,请全价购买")
    else:
        print(f"你是{age}岁,你可以免费游玩")       