from pathlib import Path



cats = Path("cats.txt")
catstxt = cats.read_text()

catstxt.count("cecar")