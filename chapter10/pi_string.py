from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    # pi_string += line
    pi_string += line.lstrip()

# print(pi_string)
# print(f"字符串的长度是{len(pi_string)}")
# print("字符串的长度是"+str(len(pi_string)))

print(f"{pi_string[:52]}")
print(len(pi_string))
