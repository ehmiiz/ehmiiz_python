from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5, 1, 3, 3, 7]

path = Path("numbers.json")

contents = path.read_text()

numbers = json.loads(contents)

print(numbers)

