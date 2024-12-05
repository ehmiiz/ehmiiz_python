from pathlib import Path

# Store file in memory
file_path = Path('learnt.txt')
file_content = Path.read_bytes(file_path)

# Print the entire file
print(file_content)

# Print file line-by-line
for line in file_content.splitlines():
    msg = str(line)
    msg = msg.replace("python", "C")
    print(msg)