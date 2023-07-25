from pathlib import Path

# path = Path('D:/A-professional/VScode/VScode-projects_python/example1/chapter10/pi_digits.txt')
path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(f"这是第{lines.index(line)+1}行:")
    print(line)
# print(contents)