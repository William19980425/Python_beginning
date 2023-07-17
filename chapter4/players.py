#切片 list[index1:index2]
players = ["charles","martina","michale","florence","eli"] 
print(players[-3:])

#print(players[:5])
players = ["charles","martina","michale","florence","eli"]
print("这里是我们的前三名队员")
for player in players[:3]:
    print(player.title())

print("这里是我们后三名的队员")
players = ["charles","martina","michale","florence","eli"]
for player in players[-3:]:
    print(player.title())

