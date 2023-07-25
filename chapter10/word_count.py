from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry,the file {path} dose not exist")
        pass # pass可以用来让Python什么都不做
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words")

filenames = ['alice.txt','harrypoter.txt','ringking.txt']
for filename in filenames:
    path =Path(filename)
    count_words(path)