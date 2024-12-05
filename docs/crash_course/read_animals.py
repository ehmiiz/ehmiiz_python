from pathlib import Path


try:
    cats = Path("cats.txt")
    dogs = Path("dogs.txt")
    
    
    cat_text = cats.read_text()
    print(cat_text)
    
    dog_text = dogs.read_text()
    print(dog_text)

except FileNotFoundError:
    pass