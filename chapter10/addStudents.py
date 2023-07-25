def addStudents(table,**students):
    print(type(students))
    for name,age in students.items():
        table[name] = age

table1 = {}
table2 = {}
addStudents(table1, 李白=20, 杜甫=24)
addStudents(table2, Jodan=45, James=32, onil=40)

print(table1)
print('----------------')
print(table2)