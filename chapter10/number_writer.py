from pathlib import Path
import json

numbers = [2,3,5,6,8,12,15]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
