even_numbers = list(range(2,11,2)) #range()还可以指定步长,第三个参数的值即为步长
print(even_numbers)

squares = []
for value in range(1,11,2):
    square = value ** 2
    squares.append(square)
print(squares)

