from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
nr = 1
for line in contents.splitlines():
    print(f"im line nr {nr}")
    print(line)
    nr += 1