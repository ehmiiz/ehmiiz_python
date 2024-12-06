# run mypy on me
# resolve using pydantic
from pydantic import validate_arguments
def math_yo(a: int, b: int) -> int:
    return a + b

# 10
print(math_yo(5,5))

# type error
print(math_yo(5,"5"))